# variables

river = 0
thunder = 0
wind = 0
shadow = 0
sky = 0
star = 0
pet = 0
rogue = 0
sisters = 0
dark_forest = 0
tribe = 0

# questions

def question14 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I will fight if I have to. It is at least a little fun.")
    print ("B. I don't want to fight. I will not hurt others.")
    print ("")
    answer14 = input ("")
    if answer14 == "A" or answer14 == "a" or answer14 == "A." or answer14 == "a." :
        rogue += 1.5
        pet -= 1.5
        star += .5
        river += .5
        shadow += .7
        sky += .6
        thunder += .6
        wind += .4
        sisters -= 1
        dark_forest += 2.5
        tribe -= 1
    elif answer14 == "B" or answer14 == "b" or answer14 == "B." or answer14 == "b." :
        rogue -= 1
        pet += 1.5
        star -= .5
        river -= .5
        shadow -= .7
        sky -= .6
        thunder -= .6
        wind -= .4
        sisters += 1
        dark_forest -= 2.5
        tribe += 1

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer14 = input ("")
        if redoanswer14 == "A" or redoanswer14 == "a" or redoanswer14 == "A." or redoanswer14 == "a." :
            rogue -= .5
            pet -= .5
            star += 1.5
            river += .5
            shadow -= .5
            sky -= .5
            thunder += .5
            wind += .5
            sisters += 1
            dark_forest += .5
            tribe -= 1.5
        elif redoanswer14 == "B" or redoanswer14 == "b" or redoanswer14 == "B." or redoanswer14 == "b." :
            rogue += 1
            pet += 1
            star -= 1
            river -= .5
            shadow += .5
            sky += .5
            thunder -= .5
            wind -= .5
            sisters -= 1
            dark_forest -= .5
            tribe += 1

def question13 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I am fine with change. If it is meant to happen, let it.")
    print ("B. I dislike change. If something is fine, why mess with it?")
    print ("")
    answer13 = input ("")
    if answer13 == "A" or answer13 == "a" or answer13 == "A." or answer13 == "a." :
        rogue -= .5
        pet -= .5
        star += 1.5
        river += .5
        shadow -= .5
        sky -= .5
        thunder += .5
        wind += .5
        sisters += 1
        dark_forest += .5
        tribe -= 1.5
    elif answer13 == "B" or answer13 == "b" or answer13 == "B." or answer13 == "b." :
        rogue += 1
        pet += 1
        star -= 1
        river -= .5
        shadow += .5
        sky += .5
        thunder -= .5
        wind -= .5
        sisters -= 1
        dark_forest -= .5
        tribe += 1

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer13 = input ("")
        if redoanswer13 == "A" or redoanswer13 == "a" or redoanswer13 == "A." or redoanswer13 == "a." :
            rogue -= .5
            pet -= .5
            star += 1.5
            river += .5
            shadow -= .5
            sky -= .5
            thunder += .5
            wind += .5
            sisters += 1
            dark_forest += .5
            tribe -= 1.5
        elif redoanswer13 == "B" or redoanswer13 == "b" or redoanswer13 == "B." or redoanswer13 == "b." :
            rogue += 1
            pet += 1
            star -= 1
            river -= .5
            shadow += .5
            sky += .5
            thunder -= .5
            wind -= .5
            sisters -= 1
            dark_forest -= .5
            tribe += 1
    question14 ()

def question12 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I follow all the rules and leader's authority, without questioning it.")
    print ("B. I don't like following rules or other cat's orders.")
    print ("")
    answer12 = input ("")
    if answer12 == "A" or answer12 == "a" or answer12 == "A." or answer12 == "a." :
        rogue -= 2
        pet -= .8
        star += 1.5
        river += 1
        shadow += .9
        sky += 1
        thunder += 1.2
        wind += 1
        sisters += .8
        dark_forest -= 1.5
        tribe += 1
    elif answer12 == "B" or answer12 == "b" or answer12 == "B." or answer12 == "b." :
        rogue += 2
        pet += .9
        star -= 1.5
        river -= 1
        shadow -= .8
        sky -= 1
        thunder -= 1.2
        wind -= 1
        sisters -= .7
        dark_forest += 1.5
        tribe -= 1

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer12 = input ("")
        if redoanswer12 == "A" or redoanswer12 == "a" or redoanswer12 == "A." or redoanswer12 == "a." :
            rogue -= 2
            pet -= .8
            star += 1.5
            river += 1
            shadow += .9
            sky += 1
            thunder += 1.2
            wind += 1
            sisters += .8
            dark_forest -= 1.5
            tribe += 1
        elif redoanswer12 == "B" or redoanswer12 == "b" or redoanswer12 == "B." or redoanswer12 == "b." :
            rogue += 2
            pet += .9
            star -= 1.5
            river -= 1
            shadow -= .8
            sky -= 1
            thunder -= 1.2
            wind -= 1
            sisters -= .7
            dark_forest += 1.5
            tribe -= 1
    question13 ()

def question11 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I enjoy jumping high and do not fear height.")
    print ("B. Going too high is scary! I don't want to get hurt.")
    print ("")
    answer11 = input ("")
    if answer11 == "A" or answer11 == "a" or answer11 == "A." or answer11 == "a." :
        rogue += .5
        pet -= .5
        star += .5
        river += .1
        shadow += 1
        sky += 2.5
        thunder += 1
        wind += .1
        sisters += .5
        dark_forest += .7
        tribe += 1
    elif answer11 == "B" or answer11 == "b" or answer11 == "B." or answer11 == "b." :
        rogue -= .5
        pet += .5
        star -= .5
        river -= .1
        shadow -= 1
        sky -= 2
        thunder -= 1
        wind -= .1
        sisters -= .5
        dark_forest -= .7
        tribe -= 1

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer11 = input ("")
        if redoanswer11 == "A" or redoanswer11 == "a" or redoanswer11 == "A." or redoanswer11 == "a." :
            rogue += .5
            pet -= .5
            star += .5
            river += .1
            shadow += 1
            sky += 2.5
            thunder += 1
            wind += .1
            sisters += .5
            dark_forest += .7
            tribe += 1
        elif redoanswer11 == "B" or redoanswer11 == "b" or redoanswer11 == "B." or redoanswer11 == "b." :
            rogue -= .5
            pet += .5
            star -= .5
            river -= .1
            shadow -= 1
            sky -= 2
            thunder -= 1
            wind -= .1
            sisters -= .5
            dark_forest -= .7
            tribe -= 1
    question12 ()

def question10 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I will intervene and help myself and others, even if they don't ask me to.")
    print ("B. I will let the situation play out even if others suffer because of it. Let other cat's futures lie in their own paws.")
    print ("")
    answer10 = input ("")
    if answer10 == "A" or answer10 == "a" or answer10 == "A." or answer10 == "a." :
        rogue -= 1
        pet -= 1
        star -= 1
        river -= .5
        shadow -= .5
        sky -= .5
        thunder += 1.2
        wind += .5
        sisters -= 1
        dark_forest -= 2
        tribe -= .5
    elif answer10 == "B" or answer10 == "b" or answer10 == "B." or answer10 == "b." :
        rogue += 1
        pet += 1
        star += 2
        river += .5
        shadow += 1
        sky += 1
        thunder -= 1.5
        wind -= .1
        sisters += 1
        dark_forest += 1.4
        tribe += .8

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer10 = input ("")
        if redoanswer10 == "A" or redoanswer10 == "a" or redoanswer10 == "A." or redoanswer10 == "a." :
            rogue -= 1
            pet -= 1
            star -= 1
            river -= .5
            shadow -= .5
            sky -= .5
            thunder += 1.2
            wind += .5
            sisters -= 1
            dark_forest -= 2
            tribe -= .5
        elif redoanswer10 == "B" or redoanswer10 == "b" or redoanswer10 == "B." or redoanswer10 == "b." :
            rogue += 1
            pet += 1
            star += 2
            river += .5
            shadow += 1
            sky += 1
            thunder -= 1.5
            wind -= .1
            sisters += 1
            dark_forest += 1.4
            tribe += .8
    question11 ()

def question9 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. If somecat wrongs me, I will get my revenge. I will make them feel what I felt. Its just justice.")
    print ("B. I will forgive other's actions, or at least not take action.")
    print ("")
    answer9 = input ("")
    if answer9 == "A" or answer9 == "a" or answer9 == "A." or answer9 == "a." :
        rogue += 1
        pet -= .5
        star -= .5
        river -= .5
        shadow -= .5
        sky -= .5
        thunder -= .5
        wind -= .5
        sisters -= .5
        dark_forest += 1.5
        tribe += .5
    elif answer9 == "B" or answer9 == "b" or answer9 == "B." or answer9 == "b." :
        rogue -= 1
        pet += .5
        star += .5
        river += 1
        shadow += 1
        sky += 1
        thunder += 1
        wind += 1
        sisters -= .5
        dark_forest -= 1.5
        tribe -= .5

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer9 = input ("")
        if redoanswer9 == "A" or redoanswer9 == "a" or redoanswer9 == "A." or redoanswer9 == "a." :
            rogue += 1
            pet -= .5
            star -= .5
            river -= .5
            shadow -= .5
            sky -= .5
            thunder -= .5
            wind -= .5
            sisters -= .5
            dark_forest += 1.5
            tribe += .5
        elif redoanswer9 == "B" or redoanswer9 == "b" or redoanswer9 == "B." or redoanswer9 == "b." :
            rogue -= 1
            pet += .5
            star += .5
            river += 1
            shadow += 1
            sky += 1
            thunder += 1
            wind += 1
            sisters -= .5
            dark_forest -= 1.5
            tribe -= .5
    question10 ()

def question8 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I will take prey, or do anything else I have to, if it means I and the others I care about survive.")
    print ("B. I will only do things inside of the Warrior Code's boundaries, even if it means I will suffer.")
    print ("")
    answer8 = input ("")
    if answer8 == "A" or answer8 == "a" or answer8 == "A." or answer8 == "a." :
        rogue += 1.5
        pet += .5
        star -= 1
        river -= .5
        shadow -= .5
        sky -= .5
        thunder -= .5
        wind -= .5
        sisters += .5
        dark_forest += 1.5
        tribe += .5
    elif answer8 == "B" or answer8 == "b" or answer8 == "B." or answer8 == "b." :
        rogue -= 2
        pet -= 1
        star += 1.1
        river += 1
        shadow += 1
        sky += 1
        thunder += 1
        wind += 1
        sisters -= 1
        dark_forest -= 1.5
        tribe -= .5

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer8 = input ("")
        if redoanswer8 == "A" or redoanswer8 == "a" or redoanswer8 == "A." or redoanswer8 == "a." :
            rogue += 1.5
            pet += .5
            star -= 1
            river -= .5
            shadow -= .5
            sky -= .5
            thunder -= .5
            wind -= .5
            sisters += .5
            dark_forest += 1.5
            tribe += .5
        elif redoanswer8 == "B" or redoanswer8 == "b" or redoanswer8 == "B." or redoanswer8 == "b." :
            rogue -= 2
            pet -= 1
            star += 1.1
            river += 1
            shadow += 1
            sky += 1
            thunder += 1
            wind += 1
            sisters -= 1
            dark_forest -= 1.5
            tribe -= .5
    question9 ()

def question7 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I have a deep connection to the land and I will stay here.")
    print ("B. I don't care where I live as long as I have my necessities and the cats I care about.")
    print ("")
    answer7 = input ("")
    if answer7 == "A" or answer7 == "a" or answer7 == "A." or answer7 == "a." :
        rogue -= 1.5
        pet += 1
        star += .5
        river += .5
        shadow += 1
        sky += .5
        thunder += 1
        wind += 1
        sisters -= 1
        dark_forest -= .5
        tribe += 1.5
    elif answer7 == "B" or answer7 == "b" or answer7 == "B." or answer7 == "b." :
        rogue += 1.5
        pet -= 1
        star -= .5
        river -= 1
        shadow -= 1
        sky -= .5
        thunder -= 1
        wind -= 1
        sisters += 1
        dark_forest += 5
        tribe -= 1.5

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer7 = input ("")
        if redoanswer7 == "A" or redoanswer7 == "a" or redoanswer7 == "A." or redoanswer7 == "a." :
            rogue -= 1.5
            pet += 1
            star += .5
            river += .5
            shadow += 1
            sky += .5
            thunder += 1
            wind += 1
            sisters -= 1
            dark_forest -= .5
            tribe += 1.5
        elif redoanswer7 == "B" or redoanswer7 == "b" or redoanswer7 == "B." or redoanswer7 == "b." :
            rogue += 1.5
            pet -= 1
            star -= .5
            river -= 1
            shadow -= 1
            sky -= .5
            thunder -= 1
            wind -= 1
            sisters += 1
            dark_forest += 5
            tribe -= 1.5
    question8 ()

def question6 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I value speed and running above most other things.")
    print ("B. I don't need to be able to run fast if I can fight.")
    print ("")
    answer6 = input ("")
    if answer6 == "A" or answer6 == "a" or answer6 == "A." or answer6 == "a." :
        rogue -= .5
        pet += .5
        star += .5
        river -= 1
        shadow -= .5
        sky -= .5
        thunder -= .5
        wind += 1.5
        sisters -= .5
        dark_forest -= .5
        tribe -= 1
    elif answer6 == "B" or answer6 == "b" or answer6 == "B." or answer6 == "b." :
        rogue += .5
        pet -= 1
        star -= .5
        river += .5
        shadow += .5
        sky += .5
        thunder += .5
        wind -= 1
        sisters += .5
        dark_forest += 1.5
        tribe -= .5

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer6 = input ("")
        if redoanswer6 == "A" or redoanswer6 == "a" or redoanswer6 == "A." or redoanswer6 == "a." :
            rogue -= .5
            pet += .5
            star += .5
            river -= 1
            shadow -= .5
            sky -= .5
            thunder -= 5
            wind += 1.5
            sisters -= .5
            dark_forest -= .5
            tribe -= 1
        elif redoanswer6 == "B" or redoanswer6 == "b" or redoanswer6 == "B." or redoanswer6 == "b." :
            rogue += .5
            pet -= 1
            star -= .5
            river += .5
            shadow += .5
            sky += .5
            thunder += .5
            wind -= 1
            sisters += .5
            dark_forest += 1.5
            tribe -= .5
    question7 ()

def question5 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I like sneaking up on my enemies to ensure victory.")
    print ("B. I prefer fighting head on, even if I am less likely to win.")
    print ("")
    answer5 = input ("")
    if answer5 == "A" or answer5 == "a" or answer5 == "A." or answer5 == "a." :
        rogue += 1.1
        pet += .5
        star -= .5
        river -= .5
        shadow += 1.5
        sky -= .5
        thunder -= 1
        wind -= .5
        sisters -= .5
        dark_forest += .5
        tribe += .5
    elif answer5 == "B" or answer5 == "b" or answer5 == "B." or answer5 == "b." :
        rogue -= .5
        pet -= .5
        star += .5
        river += 1
        shadow += .5
        sky += .5
        thunder += 1
        wind += .5
        sisters += .5
        dark_forest += 1.5
        tribe -= .5

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer5 = input ("")
        if redoanswer5 == "A" or redoanswer5 == "a" or redoanswer5 == "A." or redoanswer5 == "a." :
            rogue += 1.5
            pet += .5
            star -= .5
            river -= .5
            shadow += 1.5
            sky -= .5
            thunder -= 1
            wind -= .5
            sisters -= .5
            dark_forest += .5
            tribe += .5
        elif redoanswer5 == "B" or redoanswer5 == "b" or redoanswer5 == "B." or redoanswer5 == "b." :
            rogue -= .5
            pet -= .5
            star += .5
            river += 1
            shadow += .5
            sky += .5
            thunder += 1
            wind += .5
            sisters += .5
            dark_forest += 1.5
            tribe -= .5
    question6 ()

def question4 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I like being in or near the water and cooling off on the shore.")
    print ("B. I like keeping my paws nice and dry, thank you! Why be wet if you don't have to?")
    print ("")
    answer4 = input ("")
    if answer4 == "A" or answer4 == "a" or answer4 == "A." or answer4 == "a." :
        rogue -= .5
        pet -= 1
        star += .5
        river += 2
        shadow -= .5
        sky += .5
        thunder -= 1.5
        wind -= 1
        sisters -= .5
        dark_forest -= .5
        tribe += .5
    elif answer4 == "B" or answer4 == "b" or answer4 == "B." or answer4 == "b." :
        rogue += .5
        pet += 1
        star -= .5
        river -= 3
        shadow += .5
        sky -= .5
        thunder += 1
        wind += 1
        sisters += .5
        dark_forest += .5
        tribe -= .5

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer4 = input ("")
        if redoanswer4 == "A" or redoanswer4 == "a" or redoanswer4 == "A." or redoanswer4 == "a." :
            rogue -= .5
            pet -= 1
            star += .5
            river += 2
            shadow -= .5
            sky += .5
            thunder -= 1.5
            wind -= 1
            sisters -= .5
            dark_forest -= .5
            tribe += .5
        elif redoanswer4 == "B" or redoanswer4 == "b" or redoanswer4 == "B." or redoanswer4 == "b." :
            rogue += .5
            pet += 1
            star -= .5
            river -= 3
            shadow += .5
            sky -= .5
            thunder += 1
            wind += 1
            sisters += .5
            dark_forest -= .5
            tribe -= .5
    question5 ()

def question3 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I like having all the attention.")
    print ("B. I enjoy being in the background, with few eyes on me.")
    print ("")
    answer3 = input ("")
    if answer3 == "A" or answer3 == "a" or answer3 == "A." or answer3 == "a." :
        rogue -= 1
        pet += 2
        star += 1
        river -= .5
        shadow -= 0.5
        sky += .5
        thunder += 1
        wind -= .5
        sisters -= .5
        dark_forest += 1
        tribe -= .5
    elif answer3 == "B" or answer3 == "b" or answer3 == "B." or answer3 == "b." :
        rogue += 1
        pet -= 1.5
        star -= 1
        river += .5
        shadow += .5
        sky -= .5
        thunder -= 1
        wind += .5
        sisters += .5
        dark_forest -= 1
        tribe += .5

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer3 = input ("")
        if redoanswer3 == "A" or redoanswer3 == "a" or redoanswer3 == "A." or redoanswer3 == "a." :
            rogue -= 1
            pet += 2
            star += 1
            river -= .5
            shadow -= 0.5
            sky += .5
            thunder += 1
            wind -= .5
            sisters -= .5
            dark_forest += 1
            tribe -= .5
        elif redoanswer3 == "B" or redoanswer3 == "b" or redoanswer3 == "B." or redoanswer3 == "b." :
            rogue += 1
            pet -= 1.5
            star -= 1
            river += .5
            shadow += .5
            sky -= .5
            thunder -= 1
            wind += .5
            sisters += .5
            dark_forest -= 1
            tribe += .5
    question4 ()

def question2 ():
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe
    print ("")
    print ("A. I enjoy the snow and other cold places.")
    print ("B. I like being warm and cozy.")
    print ("")
    answer2 = input ("")
    if answer2 == "A" or answer2 == "a" or answer2 == "A." or answer2 == "a." :
        rogue += .5
        pet -= 2
        star -= 1
        river += .5
        shadow += 0.5
        sky += .5
        thunder += .5
        wind += 1
        sisters += .5
        dark_forest += 1
        tribe += 2
    elif answer2 == "B" or answer2 == "b" or answer2 == "B." or answer2 == "b." :
        rogue -= .5
        pet += 2
        star += 1
        river -=.5
        shadow -= .5
        sky -= .5
        thunder -= .5
        wind -= 1
        sisters -= .5
        dark_forest -= 1
        tribe -= 2

    else:
        print ("")
        print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
        print ("")
        redoanswer2 = input ("")
        if redoanswer2 == "A" or redoanswer2 == "a" or redoanswer2 == "A." or redoanswer2 == "a." :
            rogue += .5
            pet -= 2
            star -= 1
            river += .5
            shadow += 0.5
            sky += .5
            thunder += .5
            wind += 1
            sisters += .5
            dark_forest += 1
            tribe += 2
        elif redoanswer2 == "B" or redoanswer2 == "b" or redoanswer2 == "B." or redoanswer2 == "b." :
            rogue -= .5
            pet += 2
            star += 1
            river -=.5
            shadow -= .5
            sky -= .5
            thunder -= .5
            wind -= 1
            sisters -= .5
            dark_forest -= 1
            tribe -= 2
    question3 ()

def ending ():
    # I didn't get to make all the endings have their own message, just the most common ones.
    global river, thunder, wind, shadow, sky, star, pet, rogue, sisters, dark_forest, tribe

    # this one is if you have ONLY more pet points then any thing else. I had to change it because it was way too easy to get it.
    if pet > river and pet > thunder and pet > wind and pet > shadow and pet > sky and pet > star and pet > rogue and pet > sisters and pet > dark_forest and pet > tribe:
        print ("")
        print (f"You are going to be best as a kitty-pet {name}!")
        print ("")
        print ("In the world of warriors, Kitty-pets are two-leg(human) pets.")
        print ("Though the clans mostly think of them as lazy, some are very dangers.")
        print ("In addition, the clans slowly let more and more of them fill their ranks, including FireStar, the main character in the first series.")
        print ("Kitty-pets are kind, calm cats who usually avoid violence and look out for one another.")
        print ("You stay in one place and enjoy have only a few, strong relationships.")

    elif river >= wind and river >= thunder and river >= sky and river >= shadow and river >= sisters and river >= star and river >= rogue and river >= pet and river >= dark_forest and river >= tribe:
        print ("")
        print (f"As a Riverclan warrior, joy will find its way to you {name}!")
        print ("")

    elif thunder >= wind and thunder >= river and thunder >= sky and thunder >= shadow and thunder >= sisters and thunder >= star and thunder >= rogue and thunder >= pet and thunder >= dark_forest and thunder >= tribe:
        print ("")
        print (f"Thunderclan suits you well {name}!")

    elif shadow >= wind and shadow >= river and shadow >= sky and shadow >= dark_forest and shadow >= sisters and shadow >= star and shadow >= rogue and shadow >= pet and shadow >= thunder and shadow >= tribe:
        print ("")
        print (f"In Shadowclan, you will find what you are looking for in life {name}!")

    elif wind >= river and wind >= thunder and wind >= sky and wind >= shadow and wind >= sisters and wind >= star and wind >= rogue and wind >= pet and wind >= dark_forest and wind >= tribe:
        print ("")
        print (f"{name}, you could find much joy in living in Windclan!")

    elif sky >= river and sky >= thunder and sky >= wind and sky >= shadow and sky >= sisters and sky >= star and sky >= rogue and sky >= pet and sky >= dark_forest and sky >= tribe:
        print ("")
        print (f"As a member of Skyclan {name}, you will find happiness!")
    
    # This one, sisters, is a group that abandonds their males, so I added an extra question to make sure they are Ok with being considered female.
    elif sisters >= river and sisters >= thunder and sisters >= wind and sisters >= shadow and sisters >= sky and sisters >= star and sisters >= rogue and sisters >= pet and sisters >= dark_forest and sisters >= tribe:
        print ("")
        print ("A. I consider myself a she-cat.")
        print ("B. I am not a she-cat.\n")
        sisterQ = input ("")
        if sisterQ == "A" or sisterQ == "a" or sisterQ == "A." or sisterQ == "a." :
            print ("")
            print (f"{name}, being a sister will suit you well!")
        elif sisterQ == "B" or sisterQ == "b" or sisterQ == "B." or sisterQ == "b." :
            sisters -= 100
            ending ()
        else:
            print ("")
            print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
            print ("")
            sisterr = input ("")
            if sisterr == "A" or sisterr == "a" or sisterr == "A." or sisterr == "a." :
                print ("")
                print (f"{name}, being a sister will suit you well!")
            elif sisterr == "B" or sisterr == "b" or sisterr == "B." or sisterr == "b." :
                sisters -= 100
                ending ()

    elif rogue >= river and rogue >= thunder and rogue >= wind and rogue >= shadow and rogue >= sky and rogue >= star and rogue >= pet and rogue >= sisters and rogue >= dark_forest and rogue >= tribe:
        print ("")
        print (f"You, {name}, are a rogue or a loner at heart!")
        print ("")
        print ("In the books, rogues are described as less then amazing... but still, when passing them on travels, worriers treat them with respect and even make friends with some of them.")
        print ("Rogues enjoy going solo, without the company of others.")
        print ("They rely on themselves and no one else.")
        print ("They are travelers, and like going to new places, without lingering.")
        print ("Rogues are strong, reliable cats who may have trouble finding good relationships with others.")

    elif tribe >= river and tribe >= thunder and tribe >= wind and tribe >= shadow and tribe >= sky and tribe >= star and tribe >= rogue and tribe >= sisters and tribe >= dark_forest and tribe >= pet:
        print ("")
        print (f"It seems you will do well as a member of the Tribe Of Rushing Water {name}!")

    elif dark_forest >= wind and dark_forest >= river and dark_forest >= sky and dark_forest >= shadow and dark_forest >= sisters and dark_forest >= star and dark_forest >= rogue and dark_forest >= pet and dark_forest >= thunder and dark_forest >= tribe:
        print ("")
        print (f"You belong in the dark forest {name}...")

    elif star >= wind and star >= river and star >= sky and star >= dark_forest and star >= sisters and star >= shadow and star >= rogue and star >= pet and star >= thunder and star >= tribe:
        print ("")
        print (f"You will find freedom in Starclan {name}!")
    
    # since the only one that isn't greater than or equal to is pet, this one is only is it isn't pet, it will defalt to it. 
    else:
        print ("")
        print (f"You are going to be best as a kitty-pet {name}!")
        print ("")
        print ("In the world of warriors, Kitty-pets are two-leg(human) pets.")
        print ("Though the clans mostly think of them as lazy, some are very dangers.")
        print ("In addition, the clans slowly let more and more of them fill their ranks, including FireStar, the main character in the first series.")
        print ("Kitty-pets are kind, calm cats who usually avoid violence and look out for one another.")
        print ("You stay in one place and enjoy have only a few, strong relationships.")

print ("Hello user! I would like you to imagine you are a cat...")
print ("But not just any cat.")
print ("You are a cat in the universe of Warriors!")
print ("What would be your name in this universe. You don't need to be a warrior!")
print ("")
name = input ("")
print ("")
print (f"So, answer the following questions as you, but imagining you, as the cat named {name}!")
print ("")
print ("A. I like being solo with some alone time.")
print ("B. I feel comfortable in a group.")
print ("")
answer_1 = input ("")
if answer_1 == "A" or answer_1 == "a" or answer_1 == "A." or answer_1 == "a." :
    rogue += 1.4
    pet += 1
    star -= 0.5
    shadow -= 1
    sky -= .5
    thunder -= 1.5
    wind -= 1
    sisters -= 1
    dark_forest += .5
    tribe -= 1
elif answer_1 == "B" or answer_1 == "b" or answer_1 == "B." or answer_1 == "b." :
    rogue -= 2
    star += 1
    sky += 1
    shadow += 1
    wind += 1
    thunder += 1.5
    river += 1
    pet -= .5
    sisters += 1.5
    dark_forest -= 1
    tribe += 1
else:
    print ("")
    print (f"Hmmm... Looks like you didn't choose one of the options {name}. Just type a or b, not the whole sentence, okay?")
    print ("")
    redoanswer1 = input ("")
    if redoanswer1 == "A" or redoanswer1 == "a" or redoanswer1 == "A." or redoanswer1 == "a." :
        rogue += 2
        pet += 1
        star -= 0.5
        shadow -= 0.5
        sky -= .5
        thunder -= 1
        wind -= .5
        sisters -= 1
        dark_forest += .5
        tribe -= .5
    elif redoanswer1 == "B" or redoanswer1 == "b" or redoanswer1 == "B." or redoanswer1 == "b." :
        rogue -= 1.5
        star += .5
        sky += .5
        shadow += .5
        wind += .5
        thunder += 1
        river += .5
        pet -= .5
        sisters += 1
        dark_forest -= .5
        tribe += .5
question2 ()
ending ()






