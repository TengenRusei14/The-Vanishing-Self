# Core Blackjack game logic functions.
init python:

    def create_deck():
        """Creates and returns a standard 52-card deck."""
        suits = ["♠", "♥", "♦", "♣"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return [(r, s) for s in suits for r in ranks]

    def card_value(card):
        """Returns the numerical value of a card. Aces are counted as 11 initially."""
        rank, _ = card
        if rank in ["J", "Q", "K"]:
            return 10
        elif rank == "A":
            return 11
        return int(rank)

    def hand_value(hand):
        """Calculates the total value of a hand, adjusting for Aces if the total exceeds 21."""
        total = 0
        aces = 0
        for c in hand:
            val = card_value(c)
            total += val
            if c[0] == "A":
                aces += 1
        
        # If the hand is a bust but contains an Ace, convert the Ace's value from 11 to 1.
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def card_to_filename(card):
        """Converts a card tuple (e.g., ('K', '♠')) to its image filename (e.g., 'king_of_spades.png')."""
        rank, suit = card
        
        rank_map = {
            "A": "ace",
            "J": "jack",
            "Q": "queen",
            "K": "king"
        }
        rank = rank_map.get(rank, rank).lower()

        suit_map = {
            "♠": "spades",
            "♥": "hearts",
            "♦": "diamonds",
            "♣": "clubs"
        }
        suit = suit_map[suit]

        return f"{rank}_of_{suit}.png"

# Manages the card sound effects.
init python:
    # Keeps track of the next sound to play.
    card_sfx_index = 0

    def play_card_sound():
        """Plays card sound effects sequentially from the `card_sfx_list`."""
        global card_sfx_index

        sound_to_play = card_sfx_list[card_sfx_index]
        renpy.play(sound_to_play, channel="sound")

        # Advance the index, wrapping around to the beginning if necessary.
        card_sfx_index = (card_sfx_index + 1) % len(card_sfx_list)

default total_bet = 0

# The main entry point for the Blackjack minigame.
label blackjack:
    # Syncs the player's main game money with the minigame's internal money variable.
    python:
        if bj_user_money_variable is not None:
            bj_player_money = getattr(store, bj_user_money_variable)

    # Hides the main dialogue window for a clean UI.
    window hide

    # Proceeds to the betting phase.
    jump blackjack_betting_loop

# Handles the player's betting actions.
label blackjack_betting_loop:
    # Displays the betting screen and waits for player input.
    call screen blackjack_betting_screen(p_player_money=bj_player_money, p_total_bet=total_bet)

    # Routes the game flow based on the screen's return value.
    if _return == "deal":
        jump blackjack_start_game
    elif _return == "quit":
        jump blackjack_ended
    elif _return == "reset":
        # Resets the bet amount and returns to the betting screen.
        $ total_bet = 0
        jump blackjack_betting_loop
    else:
        # Adds the selected chip value to the total bet.
        $ total_bet += _return
        jump blackjack_betting_loop

# Sets up the game state after betting is complete.
label blackjack_start_game:
    # --- Game Setup ---
    # Disables rollback during a hand, based on user settings.
    $ _rollback = bj_allow_rollback
    # Creates and shuffles a new deck.
    $ deck = create_deck()
    $ renpy.random.shuffle(deck)
    # Resets hands and game state.
    $ player_hand = []
    $ dealer_hand = []
    $ result = None
    $ player_new_card_index = -1
    $ dealer_new_card_index = -1

    # Begins the card dealing sequence.
    call blackjack_deal_animation
    jump blackjack_turn

# Animates the initial dealing of cards.
label blackjack_deal_animation:
    $ player_hand.clear()
    $ dealer_hand.clear()

    # Show the empty table.
    show screen blackjack_ui(player_hand, dealer_hand, show_buttons=False)
    pause 0.3

    # Deal the first four cards one by one with pauses for visual effect.
    $ dealer_hand.append(deck.pop())
    $ play_card_sound()
    show screen blackjack_ui(player_hand, dealer_hand, show_buttons=False, dealer_new_card_index=0)
    pause 0.3

    $ player_hand.append(deck.pop())
    $ play_card_sound()
    show screen blackjack_ui(player_hand, dealer_hand, show_buttons=False, player_new_card_index=0)
    pause 0.3

    $ dealer_hand.append(deck.pop())
    $ play_card_sound()
    show screen blackjack_ui(player_hand, dealer_hand, show_buttons=False, dealer_new_card_index=1)
    pause 0.3

    $ player_hand.append(deck.pop())
    $ play_card_sound()
    show screen blackjack_ui(player_hand, dealer_hand, show_buttons=False, player_new_card_index=1)
    pause 0.3
    
    # Reset indices used for card animations.
    $ player_new_card_index = -1
    $ dealer_new_card_index = -1

    # Display the Hit/Stand buttons to begin the player's turn.
    show screen blackjack_ui(player_hand, dealer_hand, show_buttons=True)
    return

# Manages the player's turn.
label blackjack_turn:
    $ player_total = hand_value(player_hand)
    $ dealer_total = hand_value(dealer_hand)

    # Check for an initial Blackjack (21 on first two cards).
    if player_total == 21 and len(player_hand) == 2:
        if dealer_total == 21 and len(dealer_hand) == 2:
            $ result = "tie"
        else:
            $ result = "player_blackjack"
        jump blackjack_end

    # If player's hand reaches 21, they automatically stand.
    if player_total == 21:
        jump blackjack_dealer

    # Check if player has busted.
    if player_total > 21:
        $ result = "lose"
        jump blackjack_end

    # Wait for the player to either "Hit" or "Stand".
    call screen blackjack_ui(player_hand, dealer_hand, show_buttons=True)

    if _return == "hit":
        jump blackjack_hit
    elif _return == "stand":
        jump blackjack_dealer

# Handles the "Hit" action.
label blackjack_hit:
    # Adds a new card to the player's hand.
    $ player_hand.append(deck.pop())
    $ play_card_sound()
    # Set index to animate the newly dealt card.
    $ player_new_card_index = len(player_hand) - 1
    show screen blackjack_ui(player_hand, dealer_hand, show_buttons=False, player_new_card_index=player_new_card_index)
    pause 0.5

    # Return to re-evaluate the player's hand.
    jump blackjack_turn

# Manages the dealer's turn after the player stands.
label blackjack_dealer:
    # Hide player action buttons.
    show screen blackjack_ui(player_hand, dealer_hand, show_buttons=False)
    pause 0.25

    # Reveal the dealer's face-down card.
    show screen blackjack_ui(player_hand, dealer_hand, reveal_dealer=True, show_buttons=False)
    with dissolve
    pause 0.5

    # Dealer hits until their hand value is 17 or more.
    while hand_value(dealer_hand) < 17 and hand_value(dealer_hand) <= hand_value(player_hand):
        $ dealer_hand.append(deck.pop())
        $ play_card_sound()
        $ dealer_new_card_index = len(dealer_hand) - 1
        show screen blackjack_ui(player_hand, dealer_hand, reveal_dealer=True, show_buttons=False, dealer_new_card_index=dealer_new_card_index)
        pause 0.5
    
    $ dealer_new_card_index = -1

    # --- Determine Outcome ---
    $ dealer_total = hand_value(dealer_hand)
    $ player_total = hand_value(player_hand)

    if dealer_total > 21 or player_total > dealer_total:
        $ result = "win"
    elif dealer_total > player_total:
        $ result = "lose"
    else:
        $ result = "tie"

    jump blackjack_end

# Processes the result of the hand, calculates payouts, and displays the outcome.
label blackjack_end:
    # --- Payouts & Result Messages ---
    if result == "player_blackjack":
        play sound sound_bj_win
        $ blackjack_payout = int(total_bet * 1.5)
        $ bj_player_money += blackjack_payout
        $ result_text = f"Blackjack! You win {{color=#00FF00}}${blackjack_payout}{{/color}}!"
    elif result == "win":
        play sound sound_bj_win
        $ bj_player_money += total_bet
        $ result_text = f"You beat the dealer! You win {{color=#00FF00}}${total_bet}{{/color}}!"
    elif result == "lose":
        play sound sound_bj_lose
        $ bj_player_money -= total_bet
        $ result_text = f"You lose. The dealer takes {{color=#FF0000}}${total_bet}{{/color}}."
    else: # Tie
        play sound sound_bj_chip
        $ result_text = "A tie... your bet is returned."

    # Display the final hands and the result message.
    show screen blackjack_ui(player_hand, dealer_hand, reveal_dealer=True, result=result_text, show_buttons=False)
    pause

    # Hide the game UI.
    hide screen blackjack_ui

    # Return to the betting screen for a new hand.
    jump blackjack_betting_loop

# Executed when the player chooses to quit the game.
label blackjack_ended:
    # Syncs the minigame's money back to the player's main game money variable.
    python:
        if bj_user_money_variable is not None:
            setattr(store, bj_user_money_variable, bj_player_money)

    # Restore the dialogue window and re-enable rollback if specified.
    window show
    $ _rollback = bj_reenable_rollback_after_minigame

    return