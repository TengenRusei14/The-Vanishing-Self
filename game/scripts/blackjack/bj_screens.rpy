# The main user interface for the Blackjack game table.
# It displays cards, scores, results, and action buttons.
screen blackjack_ui(player_hand, dealer_hand, reveal_dealer=False, result=None, show_buttons=True, player_new_card_index=-1, dealer_new_card_index=-1):

    # Main container for vertical alignment.
    vbox:
        spacing 15
        xalign 0.5
        yalign 0.5

        # --- Dealer's Area ---

        # Displays the dealer's cards.
        fixed:
            ysize 160
            xfill True
            yalign 0.5
            yoffset -100
            grid 11 1:
                spacing 10
                xalign 0.5
                xoffset (750 if len(dealer_hand) > 4 else 950)

                # Loop through the dealer's hand to show each card.
                for i, card in enumerate(dealer_hand):
                    # Show the card face up if it's the first card or if the hand is revealed.
                    if i == 0 or reveal_dealer:
                        $ filename = card_to_filename(card)
                        # Animate the card if it's newly dealt.
                        if i == dealer_new_card_index:
                            add "images/blackjack/[filename]" zoom 0.4 at card_anim
                        else:
                            add "images/blackjack/[filename]" zoom 0.4
                    # Otherwise, show the card back.
                    else:
                        if i == dealer_new_card_index:
                            add "images/blackjack/card_back.png" zoom 0.4 at card_anim
                        else:
                            add "images/blackjack/card_back.png" zoom 0.4

        # Displays the dealer's score.
        fixed:
            ysize 40
            xfill True
            yalign 0.5
            yoffset 30
            if len(dealer_hand) > 1:
                # Show full total if revealed, otherwise only show the value of the first card.
                if reveal_dealer:
                    $ dealer_total = hand_value(dealer_hand)
                    text "Dealer's Cards: {color=#00FF00}[dealer_total]{/color}" size 30 xalign 0.5 style "blackjack_gui_text"
                else:
                    $ dealer_first_card_value = card_value(dealer_hand[0])
                    text "Dealer's Cards: {color=#00FF00}[dealer_first_card_value]{/color}" size 30 xalign 0.5 style "blackjack_gui_text"

        # --- Player's Area ---

        # Displays the player's score.
        fixed:
            ysize 40
            xfill True
            yalign 0.5
            yoffset 60
            if len(player_hand) > 1:
                $ player_total = hand_value(player_hand)
                text "Your Cards: {color=#00FF00}[player_total]{/color}" size 30 xalign 0.5 style "blackjack_gui_text"

        # Displays the player's cards.
        fixed:
            ysize 160
            xfill True
            yalign 0.5
            yoffset 60
            grid 11 1:
                spacing 10
                xalign 0.5
                # Dynamically adjust card position for better layout with more cards.
                xoffset (750 if len(player_hand) > 4 else 950)
                
                # Loop through the player's hand to show each card.
                for i, card in enumerate(player_hand):
                    $ filename = card_to_filename(card)
                    # Animate the card if it's newly dealt.
                    if i == player_new_card_index:
                        add "images/blackjack/[filename]" zoom 0.4 at card_anim
                    else:
                        add "images/blackjack/[filename]" zoom 0.4

        # Displays the outcome of the hand (win, lose, tie).
        fixed:
            ysize 45
            xfill True
            yalign 0.5
            yoffset 200
            if result:
                text "[result]" size 35 xalign 0.5 color "#FFD700" style "blackjack_gui_text"

    # --- Player Action Buttons ---
    if show_buttons:
        vbox:
            spacing 30
            anchor (0.0, 0.5)
            xpos 250
            ypos 0.5
            button:
                style "blackjack_button"
                text "Hit" align (0.5, 0.5) style "blackjack_gui_text"
                action Return("hit")
                at anim_hitstand
            button:
                style "blackjack_button"
                text "Stand" align (0.5, 0.5) style "blackjack_gui_text"
                action Return("stand")
                at anim_hitstand

    # --- Top Bar Info ---
    text "Total bet amount: {color=#FFD700}$[total_bet]{/color}" xalign 0.5 yanchor 0.5 yoffset 50 style "blackjack_top_text"
    text "Money: {color=#00FF00}$[bj_player_money]{/color}" xoffset 20 yanchor 0.5 yoffset 50 style "blackjack_top_text"


# The betting screen displayed before a hand starts.
screen blackjack_betting_screen(p_player_money, p_total_bet):

    # Prevents interaction with other elements behind this screen.
    modal True

    # Main container for vertical alignment.
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        # Displays the player's money and current bet amount.
        text f"Your Money: {{color=#00FF00}}${p_player_money}{{/color}}" size 40 color "#ffffff" xalign 0.5 style "blackjack_gui_text"
        text f"Current Bet: {{color=#00FF00}}${p_total_bet}{{/color}}" size 50 color "#FFD700" xalign 0.5 style "blackjack_gui_text"

        # --- Betting Chips ---
        hbox:
            xalign 0.5
            spacing 20

            # Chip for first bet option
            button:
                xysize (91, 91)
                background "images/blackjack/pokerchip1.png"
                hover_background "images/blackjack/pokerchip1.png"
                at anim_button
                action [Play("sound", sound_bj_chip), Return(bet_option1)]
                text "[bet_option1]":
                    style "blackjack_chip_text"

            # Chip for second bet option
            button:
                xysize (91, 91)
                background "images/blackjack/pokerchip2.png"
                hover_background "images/blackjack/pokerchip2.png"
                at anim_button
                action [Play("sound", sound_bj_chip), Return(bet_option2)]
                text "[bet_option2]":
                    style "blackjack_chip_text"

            # Chip for third bet option
            button:
                xysize (91, 91)
                background "images/blackjack/pokerchip3.png"
                hover_background "images/blackjack/pokerchip3.png"
                at anim_button
                action [Play("sound", sound_bj_chip), Return(bet_option3)]
                text "[bet_option3]":
                    style "blackjack_chip_text"

        # --- Action Buttons ---

        # Button to clear the current bet.
        button:
            style_prefix "blackjack"
            at anim_button
            align (0.5, 0.5)
            text "Clear bet":
                # Change text color to indicate if the button is active.
                if p_total_bet > 0:
                    color "#ffffff"
                else:
                    color "#ff8080"
                align (0.5, 0.5)
                style "blackjack_gui_text"
            
            action [Play("sound", sound_bj_chip), Return("reset")]
            # The button can only be clicked if a bet has been placed.
            sensitive p_total_bet > 0

        # Container for Deal and Quit buttons.
        hbox:
            style_prefix "blackjack"
            xalign 0.5
            spacing 20

            # Button to start the hand.
            button:
                at anim_button
                text "Deal":
                    # Change text color to indicate if the button is active.
                    if p_total_bet > 0 and p_player_money >= p_total_bet:
                        color "#ffffff"
                    else:
                        color "#ff8080"
                    align (0.5, 0.5)
                    style "blackjack_gui_text"
                action [Play("sound", sound_bj_placebet), Return("deal")]
                # The button can only be clicked if a bet is placed and the player has enough money.
                sensitive p_total_bet > 0 and p_player_money >= p_total_bet

            # Button to exit the minigame.
            button:
                at anim_button
                text "Quit":
                    color "#ffffff"
                    align (0.5, 0.5)
                    style "blackjack_gui_text"
                action Return("quit")