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

    "Seems like my Father is calling me"
    pov "Coming, Father"
    "My Father who's name is Arnold Crimston work's at a meat store as a butcher, but loves to spend most of his time playing cards with his family"
    "And my Mother Elenoire Crimston is a wonderful and beutiful stay at home mom, but so are most of the other mom's living in this city"
    
    $ dadname = "Arnold Crimston"
    $ momname = "Elenoire Crimston"

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
            jump jll
        "Be rich and succesful":
            jump rns

label rns:
    pov "I want to be the richest man this world has ever seen"
    d "That's quite an ambitious dream"
    pov "I know, but I believe I can make it"
    d "So how do you plan on acheviing it son"

    menu:
        d "So how do you plan on acheviing it son"
        "I'll be a gambler":
            jump gambler
        "I'll start a business":
            jump business

label gambler:
    pov "I will become the world's best blackjack gambler and make millions from it"
    pov "No one will be able to stop me from achieving my goals"
    d "I guess with young age comes crazy ambitions"
    pov "As people say, the only thing stopping you from achieving your goals is that one big step"
    d "I don't get how that is related to what we are speaking about, But I guess it would'nt hurt to try"
    "Honestly, I spent too much time in my previous life worrying about deadlines and meeting and so many other things"
    "That I forgot that I need to enjoy life, and now that the oppurtunity has presented itself I will now dedicate my life to being a blackjack gambler"
    "And I'll be the richest amongst them all"
    d "Why not challenge me to a battle of blackjack then"
    menu:
        d "Why not challenge me to a battle of poker then"
        "Yes":
            call blackjack
        "No":
            "I'm sorry Father"
    "This still works"
    #still needs edits
    return

label business:
    "I remember being a slave to employement in my previous life and how much I suffered and toiled just to get by"
    "Now I have a chance to change that and become the man at the top"
    "Why would I refuse such an oppurtunity"
    pov "Father, I want to be a succesful entrepreuneur who will make money of his business"
    pov "And help many people who don't have job's a chance to work"
    d "That's very honorable of you son"
    d "I'm proud that you know what you want"
    #still needs edits
    return


label jll:
    pov "Father, I simply want to get a normal job and live a normal life, just like mom and you"
    pov "And maybe even start a family"
    d "And how do you plan on going about that?"

    menu:
        d "And how do you plan on going about that?"
        "Studying hard in school":
            jump normalschoolroute
        "By getting a normal job and working hard":
            jump normaljobroute

label normalschoolroute:
    pov "Studying hard in school"
    d "Well then I have great news for you"
    pov "What is it Father?"
    d "Your mother has decided to enroll you into an academy"
    pov "Really"
    d "Yes, she said it would be best if you started learning early, that's why I asked you this question son"
    "Well I guess this is the most optimal choice, since it requires less risk and is the path I took in my past life"
    #still needs edits
    return

label normaljobroute:
    pov "By getting a normal job and working hard"
    d "Then what do you think about working in the emerald mines or being a hunter"
    menu:
        "Work in emerald mines":
            jump em
        "Become a Hunter":
            jump hunter

label em:
    "Although this job has many risks I believe that the pay is decent enough to sustain both me and my family"
    "And is a job that requires less social interactions and more manual labour so it be a good choice for me"
    pov "Father I choose the Emerald Mines"
    d "Very well, I'll see what I can do"
    pov "Thank you Father"
    #still needs edits
    return

label hunter:
    "A job with no social interactions, no orders, or people to boss you around sounds way better than the job that I had in my previous life"
    "Although it requires more effort and hardwork and also connnections with people who are willing to buy your hunt for a decent price"
    "It is a fairly good job for a person like me and with my Father as a butcher it will become fairly easy"
    pov "Father I'd like to be a hunter"
    d "Hahaha, A Father who is a Butcher and a Son who is a hunter"
    d "That's a very good combination don't you think?"
    pov "Yes Father, that is part of the reason I chose this job"
    d "Very well, Hunting Training starts tomorrow"
    #still needs edits
    return
