#Characters
define pov = Character("[povname]")
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


    show black with fade
    with Pause(2)

    "Where am I?"
    m "Oh dear isnt our son cute?"
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

    scene black with fade
    with Pause(1)

    show text "10 YEARS LATER" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    "It's been 10 years since I've started a new life in this world, and there is some information I've collected during this time"
    "I am no longer on earth but on a planet named Sodom, unfortunately unlike fantasy world's there has been no signs of demon's or monster's that have existed and are simply a myth"
    "But that does not mean that this world is sunshine and rainbow's like I thought, I recently found out that a person's life span is dependant on their relationships"
    "Which are defined by an individials contribution, so the more you help a person the closer you become and the more you refuse help the more likely you are to meet death"
    "Individuals who have a zero out of 10 star relationship with at around 5 people tend to suddenly die of a unexplicable heart attack"
    
    d "[povname]!!!"

    "Seems like my Dad is calling me"
    pov "Coming, Father"
    "My Dad who's name is Arnold Crimston work's at a meat store at a butcher, but loves to spend most of his time playing cards with his family"
    "And my mom Elenoire Crimston is a wonderful and beutiful stay at home mom, but so are most of the other mom's living in this city"
    
    $ dadname = "Arnold Crimston"
    $ momname = "Elenoire Crimston"

    d "Morning Son, How are you doing"
    pov "I'm doing great Father, what about you"
    d "You know getting ready for a card game, do you want to join?"

    menu:
        "Do you wish to play cards with your Father"
        "Yes":
            jump cardgame
        "No":
            jump nocardgame

label cardgame:
    pov "Yes Father let's play"
    d "Get ready then because I won't lose again this time"
    pov "That's what you always say Father"
    #card game system
    return

label nocardgame:
    pov "I'm sorry Father, I'm kind of busy right now"
    d "Oh, I guess you don't really want to play with your old man"
    pov "It's not like that Father"
    d "No son it's ok, go carry on with what you were doing"
    d "I guess I'll just go to the local bar and maybe find someone willing to play"
    return

    return

