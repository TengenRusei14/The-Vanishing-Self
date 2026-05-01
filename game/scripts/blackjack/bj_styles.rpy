
# All styles for the different buttons and text.

style blackjack_button:
    is default
    xysize (300, None)
    background Frame("images/blackjack/choice_[prefix_]background.png",
        150, 25, 150, 25, tile=False)
    padding (12, 12)

style blackjack_top_text:
    font "Museo500.otf"
    size 40

style blackjack_gui_text:
    font "Museo500.otf"
    size 30

style blackjack_chip_text:
    font "Museo500.otf"
    align (0.5, 0.5)
    color "#FFFFFF"
    size 30


transform card_anim:
    xpos 800 ypos -800
    easeout 0.2 xpos 0 ypos 0

transform anim_button:
    on hover:
        linear 0.1 yoffset -5
    on idle:
        linear 0.1 yoffset 0

transform anim_hitstand:
    on hover:
        linear 0.1 xoffset 5
    on idle:
        linear 0.1 xoffset 0

