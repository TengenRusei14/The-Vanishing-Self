
# All the defined blackjack variables.

# If you want to allow the player to be able to roll back and "cheat" or not.
define bj_allow_rollback = False

# If you want the player to be able to roll back AFTER the minigame is finished.
define bj_reenable_rollback_after_minigame = False

# =============================================================================
# == SOUND CONFIGURATION
# =============================================================================
# You can replace these audio files or set a different path
define sound_bj_win = "audio/blackjack/bj_win.ogg" # Winning sound
define sound_bj_lose = "audio/blackjack/bj_lose.ogg" # Losing sound
define sound_bj_chip = "audio/blackjack/bj_chip.ogg" # Raising bet sound
define sound_bj_placebet = sound_bj_chip # Confirming bet sound (When pressing deal)

# When cards are placed it will play these sounds in the following order and then start over.
define sound_bj_card1 = "audio/blackjack/bj_card1.ogg"
define sound_bj_card2 = "audio/blackjack/bj_card2.ogg"
define sound_bj_card3 = "audio/blackjack/bj_card3.ogg"
define sound_bj_card4 = "audio/blackjack/bj_card4.ogg"

define card_sfx_list = [sound_bj_card1, sound_bj_card2, sound_bj_card3, sound_bj_card4]


# =============================================================================
# == MONEY CONFIGURATION
# =============================================================================

# You can change the bet chip values
define bet_option1 = 10
define bet_option2 = 100
define bet_option3 = 400

# To allow this script to use your game's existing money variable,
# change the string below to match the name of your variable.
# For example, if your money is stored in a variable called 'gold',
# change this line to: define bj_user_money_variable = "gold"
define bj_user_money_variable = "money"

# If you want this blackjack game to have its own separate money supply
# and NOT affect the player's main money, set the variable name to None, like this:
# define bj_user_money_variable = None


# This is the starting money the player will have if NOT syncing with another variable.
default bj_player_money = 1000

# =============================================================================