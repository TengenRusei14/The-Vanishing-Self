default money = 400
default slot_icons = ["seven.png", "bar.png", "banana.png"]

init python:
    import random

screen display_money():
    frame:
        xpadding 15
        ypadding 15
        xalign 0.0
        yalign 0.0

    vbox:
        text "Your money: [money]$"

label spin:
    if renpy.persistent.counter < 10:
        $ random_image_row1_indicator = renpy.random.randint(0, len(slot_icons)-1)
        $ random_image_row2_indicator = renpy.random.randint(0, len(slot_icons)-1)
        $ random_image_row3_indicator = renpy.random.randint(0, len(slot_icons)-1)

        $ random_image_row1 = slot_icons[random_image_row1_indicator]
        $ random_image_row2 = slot_icons[random_image_row2_indicator]
        $ random_image_row3 = slot_icons[random_image_row3_indicator]

        show expression Image("images/slots/" + random_image_row1):
            xalign 0.41
            yalign 0.402
        show expression Image("images/slots/" + random_image_row2):
            xalign 0.41
            yalign 0.465
        show expression Image("images/slots/" + random_image_row3):
            xalign 0.41
            yalign 0.523
        pause(0.15)

        $ renpy.persistent.counter += 1
        jump spin
    else: 
        if random_image_row1 == random_image_row2 == random_image_row3:
            r "Congratulations you win"
            if random_image_row1_indicator == 0:
                $ money = money + (int(money_bet)*100)
                $ money_bet = 0
            elif random_image_row1_indicator == 1:
                $ money = money + (int(money_bet)*10)
                $ money_bet = 0
            elif random_image_row1_indicator == 2:
                $ money = money + (int(money_bet)*5)
                $ money_bet = 0
        else:
            r "You have lost. Good luck next time"

        $ renpy.persistent.counter = 0
        return



image table1:
    "table1.png"
    fit "fill"
    xsize 4000
    ysize 4000

    xalign 0.5
    yalign 0.5

#Characters
define pov = Character("[povname]")
#Dealer
define r = Character("Rahim")
#mom
default momname = "???"
define m = Character("[momname]", color = "#db82b9")
#father
default dadname = "???"
define d = Character("[dadname]", color = "#3700ff")

label splashscreen:
    scene black
    with Pause(1)

    show text "Valerian Crow Presents" with dissolve 
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


label start:
    $ povname = renpy.input("What's your name?", length=32)
    $ povname = povname.strip()

    if not povname:
        $ povname = "Thaddeus Mahi"

    jump intro

label intro:
    scene sky_day
    "Sixteen years of school brought me to where I am today"
    "A low paying job that treated me like I was replaceable"
    "With people constantly screaming and shifting the blame onto me"
    "Where working overtime seemed like part of normal work hours"
    "And breaks felt like miracles"
    "Despite all this no one seemed to care"
    "So I decided to end it all"
    "With no achievements to carry with me to my grave"
    "And yet I wish for another life"
    "A life where I truly matter"
    hide sky_day

    show black with fade
    with Pause(2)

    scene inthallway2_evening
    "Where am I?"
    show mom at left
    m "Oh dear isnt our son cute?"
    show dad at right
    d "HAHAHA!"
    d "Of course he is my son after all"
    m "True he does take after you a lot"
    "Is this the voice of my new parents, let me try getting a glimpse of who they are"
    "I slowly opened my eyes but it was harder than expected"
    m "Look Dear! Our son opened his eyes"
    d "He has the same eyes as you dear"
    m "Don't flirt with me in front of the child dear"
    d "I'm serious"
    d "So what do we name him?"
    m "Let's call him [povname]"
    "[povname] isn't a bad name at all"
    "It's probably way better than the name I had before, What was it again, I can't remember"
    "Now that my new life has been decided time to make it count"
    hide mom
    hide dad
    hide inthallway2_evening

    scene black with fade
    with Pause(1)

    show text "10 YEARS LATER" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene bedroom01_day
    show andy at left
    "It's been 10 years since I've started a new life in this world, and there is some information I've collected during this time"
    "I am no longer on earth but on a planet named Sodom, unfortunately unlike fantasy world's there has been no signs of demon's or monster's that have existed and are simply a myth"
    "But that does not mean that this world is sunshine and rainbow's like I thought, I recently found out that a person's life span is dependant on their relationships"
    "Which are defined by an individials contribution, so the more you help a person the closer you become and the more you refuse help the more likely you are to meet death"
    "Individuals who have a zero out of 10 star relationship with at around 5 people tend to suddenly die of a unexplicable heart attack"
    
    d "[povname]!!!"

    "Seems like my Father is calling me"
    pov "Coming, Father"
    "My Father who's name is Arnold Crimston work's at a meat store as a butcher, but loves to spend most of his time playing cards with his family"
    "And my Mother Elenoire Crimston is a wonderful and beutiful stay at home mom, but so are most of the other mom's living in this city"
    hide bedroom01_day with dissolve
    $ dadname = "Arnold Crimston"
    $ momname = "Elenoire Crimston"

    scene backyard_day1
    show dad at right
    show andy at left
    d "Morning Son, How are you doing"
    pov "I'm doing great Father, what about you"
    d "Great"
    pov "Is there anything you wanted to talk about"
    d "I've just been thinking, it's been 10 years since we had you and never thought to ask you..."
    d "What is your goal in life?"
    "That question hit me like a arrow to a target, ever since I came to this world all I've been concerened about was how to live a better life than my previous one"
    "But never did I think of how, which makes me look like a fool"

    menu:
        "What do I want to do in life?"
        "Just live life":
            jump simple
        "Be rich and succesful":
            jump rns

label rns:
    pov "I want to be the richest man this world has ever seen"
    d "That's quite an ambitious dream"
    pov "I know, but I believe I can make it"
    d "So how do you plan on acheviing it son"
    pov "I am going to be a gambler"
    d "WHAAT!!!"
    d "You must be joking son"
    pov "No Father, I'm serious I wish to be a proffesional gambler"
    d "No, I will not allow you to waste your life like that"
    d "You have so much potential in you my son"
    d "And you want to waste it gambling it away"
    pov "Father"
    pov "I think therefore I am"
    pov "Going to school is a gamble, waking up everyday is a gamble, life in itself is a gamble"
    pov "So why should I try wasting it on something I don't enjoy, Why should I waste my entire life struggling"
    pov "Going through ups and downs due to job insecurity, bad workplaces and even bad employee's that's not how I want my life to turn out like"
    pov "SO YES I WILL SPEND MY LIFE GAMBLING"
    d "It's seems like you've made up your made son, I won't stop you"
    hide andy
    hide dad
    jump gambler

label simple:
    scene backyard_day1
    show dad at right
    show andy at left    
    "Honestly I don't really have that many dreams and goals, and honestly I don't mind living a very simple life"
    "As long as I am able to have a better job than my prevous life I won't have to suffer any more"
    jump end
    hide backyard_day1

label gambler:
    scene backyard_day1
    show dad at right
    show andy at left    
    d "If you truly are wanna be a gambler as you said you were, then I challenge you to a simple game of blackjack"
    "He isn't truly sure that this is the right path, but he unfortunatly has no choice but to trust in me"
    pov "Of course Father, I dont mind a challenge it's not like I'll lose or anything"
    d "Getting cocky huh?"
    d "Here's 400 silver to get you started"
    pov "Thanks Dad, game on"

    scene table1
    call blackjack
    hide table1

    if money <=0:
        jump failure
    else:
        jump casino
        hide backyard_day1

label failure:
    scene backyard_day1
    show dad at right
    show andy at left    
    d "You can't even beat me in a simple game of blackjack and you claim you wish to be a pro gambler"
    jump end
    hide backyard_day1

label casino:
    scene backyard_day1
    show dad at right
    show andy at left    
    d "Wow I guess you are ready"
    pov "I told you I was meant for this"
    d "I guess you were right there's a casino nearby let us head there"
    "We decided to pack our bags, inform my mother and departed to royal house casino"
    "I had thought the casino was close by since he had sad so but the journey was a 2 hour ride"
    "Anyway we had arrived and we were greeted by a dealer named rahim"
    jump rahim
    hide backyard_day1

label rahim:
    scene bg outcasino
    show rashim neutral at left 
    r "Welcome to Rahim Grand Casino"
    r "What would you like to play"
    hide bg outcasino
    scene bg incasino
    menu:
        "Blackjack":
            jump blackjack1
        "Roulette":
            jump roulette
        "One Hand Bandit":
            jump slots
        "Quit Rahim Grand Casino":
            jump enter_no
    hide bg incasino

label blackjack1:
    scene table1
    call blackjack
    hide table1
    jump rahim

label option_stop_playing_roulette:
    menu:
        "Do you want to stop playing?"
        "Yes":
            jump rahim
        "No":
            jump roulette

label roulette:
    show screen display_money
    hide rashim neutral
    scene bg roulette

    if money <=0:
        jump casino_kick
    
    python:
        money_bet = renpy.input("How much do you want to bet?")

    if money_bet.isdigit():
        $ money_bet = int(money_bet)
        $ money = money - money_bet
    else:
        "Do you want to stop playing"
        jump option_stop_playing_roulette

    r "Choose color you want to bet on"
    menu:
        "Black":
            jump black
        "Red":
            jump red
        "Green":
            jump green
        "Go Back":
            python:
                money = money + int(money_bet)
                money_bet = 0
            jump game_choice

label black:
    $ roulette_color = 1 
    jump roulette_spin
label red:
    $ roulette_color = 2
    jump roulette_spin
label green:
    $ roulette_color = 3
    jump roulette_spin

label roulette_spin:
    if roulette_color == 1:
        r "You chose black"
    elif roulette_color ==2:
        r "You chose red"
    else:
        r "You chose green"

$ random_numer = renpy.random.randint(1, 37)
if random_numer <= 18:
    r "Winner is black!"
    if roulette_color == 1:
        jump roulette_win
    else:
        jump roulette_lose
elif random_numer == 37:
    r "Winner color is green!"
    if roulette_color == 3:
        jump roulette_win_green
    else:
        jump roulette_lose
else:
    r "Winning color is red!"
    if roulette_color == 2:
        jump roulette_win
    else:
        jump roulette_lose

label roulette_win:
    python:
        money = money + (int(money_bet)*2)
        money_bet = 0
    show screen display_money
    r "You win! Congratulation"
    jump roulette

label roulette_win_green:
    python:
        money = money + (int(money_bet)*14)
        money_bet = 0
    show screen display_money
    r "You hit the jackpot green! Congratulation"
    jump roulette

label roulette_lose:
    r "You lose! Good luck next time"
    jump roulette

label slots:
    show screen display_money
    hide rashim neutral
    scene bg slots
    show slots_rewards:
        xalign 1.0
        yalign 0.0

label slots_next:
    show screen display_money
    if money <= 0:
        jump casino_kick
        jump casino_kick

    menu:
        "Spin":
            jump slots_next_2
        "Go Back":
            jump rahim

label slots_next_2:

    python:
        money_bet = renpy.input("How much do you want to bet?")
    if money_bet.isdigit():
        $ money_bet = int(money_bet)
        $ money = money - money_bet
    else:
        "Do you want to stop playing"
        menu:
            "Yes":
                jump rahim
            "No":
                jump slots

$ renpy.persistent.counter = 0
call spin
jump slots_next

label casino_kick:
    show screen display_money
    scene bg incasino
    with dissolve(1)
    show rashim neutral
    r "You lost all your money get out!"
    return

label enter_no:
    r "Thank you for playing hope to see you again"
    r "Bye"
    return

label end:
    scene black with fade
    with Pause(2)

    show text "You are so boring player \n You lived your entire previous life tryng to be normal \n And I gave you a chance, a chance to be a better person then you were before \n But you ruined it \n ALL FOR A NORMAL LIFE"
    with Pause(25)

    hide text with dissolve
    with Pause(2)

    return