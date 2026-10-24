import time
import random
max_health = 50
health = 50
strength = 5
num = 0
enemy = 0
power = 0
monster = 0
defense = 0
boss = 1
print ("Hello user! Today you will be playing a turn-based game!")
print ("")
print ("In a land called... sigh.")
print ("I don't feel like doing world building today.")
print ("In fact, I don't feel like making any storyline.")
print ("So, lets thrown interesting stories to the wind!")
print ("")
print ("So you can either attack or gather power every turn. If you have two power, you can use a stronger spell to do more damage.")
print ("The enemies will slowly grow stronger and after every win you can add a point to a stat.")
print ("After defeating 10 enemies, you will fight the boss!")
print ("")
print ("Ok, so you are in a dungeon bla bla bla defeat the monsters.")
print ("You are walking and boom! A monster is in your path.")
print ("Engage the enemy!")
time.sleep(2)
# this is the first 5 battles. lines 28 - 290. there's a for loop inside but I dont think I need to explain that
for i in range (5):
    print ("")
    if num == 0:
        monster = random.choice (["goblin", "orc"])
    if monster == "goblin" and num == 0:
        print ("Looks like your fighting a goblin!")
        enemy = random.choice ([25,26,27,28,29,30,31,32,33,34,35])
        est = random.choice ([5,6,7,8,9,10])
        print (f"The goblin has {enemy} health!")
        print (f"By the way you have {health} health!")
        num += 1
    if monster == "orc" and num == 0:
        print ("Looks like your fighting a orc!")
        enemy = random.choice ([30,31,32,33,34,35,36,37,38,39,40])
        est = random.choice ([6,7,8,9,10,11])
        print (f"The orc has {enemy} health!")
        print (f"By the way you have {health} health!")
        num += 1
    for i in range (100):
        if num == 1:
            print ("Hey, so you have a few options for what you can do.")
            print ("")
            print ("A. Attack!")
            print ("B. Brace/gather power!")
            if power >= 2:
                print (f"C. Power move(uses 2 power and you currently have {power} power.)")
            print ("")
            question = input ("")
            if question == "A" or question == "a" or question == "A." or question == "a." :
                print ("")
                if strength == 5:
                    hit = random.choice ([4,4,5,5,5,6,6,7])
                if strength == 6:
                    hit = random.choice ([5,5,6,6,6,7,7,8])
                if strength == 7:
                    hit = random.choice ([6,6,7,7,7,8,8,9])
                if strength == 8:
                    hit = random.choice ([7,7,8,8,8,9,9,10])
                if strength == 9:
                    hit = random.choice ([8,8,9,9,9,10,10,11])
                if strength == 10:
                    hit = random.choice ([9,9,10,10,10,11,11,12])
                if strength == 11:
                    hit = random.choice ([10,10,11,11,11,12,12,13])
                if strength == 12:
                    hit = random.choice ([11,11,12,12,12,13,13,14])
                if strength == 13:
                    hit = random.choice ([12,12,13,13,13,14,14,15])
                if strength == 14:
                    hit = random.choice ([13,13,14,14,14,15,15,16])
                if strength == 15:
                    hit = random.choice ([14,14,15,15,15,16,16,17])
                enemy -= hit
                if enemy <= 0:
                    print ("")
                else:
                    print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
            elif question == "B" or question == "b" or question == "B." or question == "b." :
                print ("")
                power += 1
                defense += 1
                print ("Ok, so you are now defending. Cool.")
                print (f"you have {power} power now.")
            elif question == "C" or question == "c" or question == "C." or question == "c." and power >= 2 :
                print ("")
                powerr = random.choice ([4,5,5,5,6,6,7])
                strength += powerr
                if strength == 5:
                    hit = random.choice ([4,4,5,5,5,6,6,7])
                if strength == 6:
                    hit = random.choice ([5,5,6,6,6,7,7,8])
                if strength == 7:
                    hit = random.choice ([6,6,7,7,7,8,8,9])
                if strength == 8:
                    hit = random.choice ([7,7,8,8,8,9,9,10])
                if strength == 9:
                    hit = random.choice ([8,8,9,9,9,10,10,11])
                if strength == 10:
                    hit = random.choice ([9,9,10,10,10,11,11,12])
                if strength == 11:
                    hit = random.choice ([10,10,11,11,11,12,12,13])
                if strength == 12:
                    hit = random.choice ([11,11,12,12,12,13,13,14])
                if strength == 13:
                    hit = random.choice ([12,12,13,13,13,14,14,15])
                if strength == 14:
                    hit = random.choice ([13,13,14,14,14,15,15,16])
                if strength == 15:
                    hit = random.choice ([14,14,15,15,15,16,16,17])
                if strength == 16:
                    hit = random.choice ([15,15,16,16,16,17,17,18])
                if strength == 17:
                    hit = random.choice ([16,16,17,17,17,18,18,19])
                if strength == 18:
                    hit = random.choice ([17,17,18,18,18,19,19,20])
                if strength == 19:
                    hit = random.choice ([18,18,19,19,19,20,20,21])
                if strength == 20:
                    hit = random.choice ([19,19,20,20,20,21,21,22])
                if strength == 21:
                    hit = random.choice ([20,20,21,21,21,22,22,23])
                if strength == 22:
                    hit = random.choice ([21,21,22,22,22,23,23,24])
                if strength == 23:
                    hit = random.choice ([22,22,23,23,23,24,24,25])
                enemy -= hit
                if enemy <= 0:
                    print ("")
                    print (f"You did {hit} damage!")
                else:
                    print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
                strength -= powerr
                power -= 2
            else:
                print ("")
                print ("Hmmm... Looks like you didn't choose one of the options. Just type a or b, not the whole sentence, okay?")
                print ("")
                redoanswer = input ("")
                if redoanswer == "A" or redoanswer == "a" or redoanswer == "A." or redoanswer == "a." :
                    print ("")
                    if strength == 5:
                        hit = random.choice ([4,4,5,5,5,6,6,7])
                    if strength == 6:
                        hit = random.choice ([5,5,6,6,6,7,7,8])
                    if strength == 7:
                        hit = random.choice ([6,6,7,7,7,8,8,9])
                    if strength == 8:
                        hit = random.choice ([7,7,8,8,8,9,9,10])
                    if strength == 9:
                        hit = random.choice ([8,8,9,9,9,10,10,11])
                    if strength == 10:
                        hit = random.choice ([9,9,10,10,10,11,11,12])
                    if strength == 11:
                        hit = random.choice ([10,10,11,11,11,12,12,13])
                    if strength == 12:
                        hit = random.choice ([11,11,12,12,12,13,13,14])
                    if strength == 13:
                        hit = random.choice ([12,12,13,13,13,14,14,15])
                    if strength == 14:
                        hit = random.choice ([13,13,14,14,14,15,15,16])
                    if strength == 15:
                        hit = random.choice ([14,14,15,15,15,16,16,17])
                    enemy -= hit
                    if enemy <= 0:
                        print ("")
                    else:
                        print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
                elif redoanswer == "B" or redoanswer == "b" or redoanswer == "B." or redoanswer == "b." :
                    print ("")
                    power += 1
                    defense += 1
                    print ("Ok, so you are now defending. Cool.")
                    print (f"you have {power} power now.")
                elif redoanswer == "C" or redoanswer == "c" or redoanswer == "C." or redoanswer == "c." and power >= 2 :
                    print ("")
                    powerr = random.choice ([4,5,5,5,6,6,7])
                    strength += powerr
                    if strength == 5:
                        hit = random.choice ([4,4,5,5,5,6,6,7])
                    if strength == 6:
                        hit = random.choice ([5,5,6,6,6,7,7,8])
                    if strength == 7:
                        hit = random.choice ([6,6,7,7,7,8,8,9])
                    if strength == 8:
                        hit = random.choice ([7,7,8,8,8,9,9,10])
                    if strength == 9:
                        hit = random.choice ([8,8,9,9,9,10,10,11])
                    if strength == 10:
                        hit = random.choice ([9,9,10,10,10,11,11,12])
                    if strength == 11:
                        hit = random.choice ([10,10,11,11,11,12,12,13])
                    if strength == 12:
                        hit = random.choice ([11,11,12,12,12,13,13,14])
                    if strength == 13:
                        hit = random.choice ([12,12,13,13,13,14,14,15])
                    if strength == 14:
                        hit = random.choice ([13,13,14,14,14,15,15,16])
                    if strength == 15:
                        hit = random.choice ([14,14,15,15,15,16,16,17])
                    if strength == 16:
                        hit = random.choice ([15,15,16,16,16,17,17,18])
                    if strength == 17:
                        hit = random.choice ([16,16,17,17,17,18,18,19])
                    if strength == 18:
                        hit = random.choice ([17,17,18,18,18,19,19,20])
                    if strength == 19:
                        hit = random.choice ([18,18,19,19,19,20,20,21])
                    if strength == 20:
                        hit = random.choice ([19,19,20,20,20,21,21,22])
                    if strength == 21:
                        hit = random.choice ([20,20,21,21,21,22,22,23])
                    if strength == 22:
                        hit = random.choice ([21,21,22,22,22,23,23,24])
                    if strength == 23:
                        hit = random.choice ([22,22,23,23,23,24,24,25])
                    enemy -= hit
                    if enemy <= 0:
                        print ("")
                        print (f"You did {hit} damage!")
                    else:
                        print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
                    strength -= powerr
                    power -= 2
                else:
                    print ("")
                    print ("OK!!! STOP BEING ANNOYING!!! JUST CHOOSE SOMETHING!!! ACTUALLY, SCRATCH THAT! LEAVE ME ALONE AND TRY AGAIN WHEN YOU CAN HANDLE THIS!!!")
                    quit ()
            time.sleep(2)
            if enemy <= 0:
                num = 0
                power = 0
                print ("You beat the enemy!")
                print (f"You still have {health} health!")
                print ("Do you want to put your upgrade points into health (fully heals you and gives +5 max. health) or strength (increases damage)?")
                print ("")
                question = input ("")
                if question == "a" or question == "A" or question == "a." or question == "A." or question == "health" or question == "Health" or question == "heal" or question == "Heal" or question == "Max. health" or question == "Max health" or question == "max. health" or question == "max health" or question == "Max. Health" or question == "Max Health":
                    print ("")
                    max_health += 5
                    health = max_health
                    print (f"Ok! now you have {health} health!")
                    print ("Onto the next battle!")
                elif question == "b" or question == "B" or question == "b." or question == "B." or question == "strength" or question == "Strength" or question == "damage" or question == "Damage" or question == "increase damage" or question == "Increase damage" or question == "Increase Damage":
                    print ("")
                    strength += 1
                    print ("You have increased your damage!")
                    print ("Onto the next battle!")
                else: 
                    print ("Hmmm... I'm not sure what you just said. Please just say something like 'health' or 'strength' or 'a' or 'b' or something along those lines.")
                    print ("")
                    redoanswer = input("")
                    if redoanswer == "a" or redoanswer == "A" or redoanswer == "a." or redoanswer == "A." or redoanswer == "health" or redoanswer == "Health" or redoanswer == "heal" or redoanswer == "Heal" or redoanswer == "Max. health" or redoanswer == "Max health" or redoanswer == "max. health" or redoanswer == "max health" or redoanswer == "Max. Health" or redoanswer == "Max Health":
                        print ("")
                        max_health += 5
                        health = max_health
                        print (f"Ok! now you have {health} health!")
                        print ("Onto the next battle!")
                    if redoanswer == "b" or redoanswer == "B" or redoanswer == "b." or redoanswer == "B." or redoanswer == "strength" or redoanswer == "Strength" or redoanswer == "damage" or redoanswer == "Damage" or redoanswer == "increase damage" or redoanswer == "Increase damage" or redoanswer == "Increase Damage":
                        print ("")
                        strength += 1
                        print ("You have increased your damage!")
                        print ("Onto the next battle!")
            else:
                print ("")
                print ("Ok. Time for the enemy to hit you!")
                if defense == 1:
                    defender = random.choice ([1,2,2,3,3,4])
                if strength == 5:
                    ehit = random.choice ([4,4,5,5,5,6,6,7])
                if strength == 6:
                    ehit = random.choice ([5,5,6,6,6,7,7,8])
                if strength == 7:
                    ehit = random.choice ([6,6,7,7,7,8,8,9])
                if strength == 8:
                    ehit = random.choice ([7,7,8,8,8,9,9,10])
                if strength == 9:
                    ehit = random.choice ([8,8,9,9,9,10,10,11])
                if strength == 10:
                    ehit = random.choice ([9,9,10,10,10,11,11,12])
                if strength == 11:
                    ehit = random.choice ([10,10,11,11,11,12,12,13])
                if strength == 12:
                    ehit = random.choice ([11,11,12,12,12,13,13,14])
                if strength == 13:
                    ehit = random.choice ([12,12,13,13,13,14,14,15])
                if strength == 14:
                    ehit = random.choice ([13,13,14,14,14,15,15,16])
                if strength == 15:
                    ehit = random.choice ([14,14,15,15,15,16,16,17])
                if strength == 16:
                    ehit = random.choice ([15,15,16,16,16,17,17,18])
                if strength == 17:
                    ehit = random.choice ([16,16,17,17,17,18,18,19])
                if strength == 18:
                    ehit = random.choice ([17,17,18,18,18,19,19,20])
                if strength == 19:
                    ehit = random.choice ([18,18,19,19,19,20,20,21])
                if strength == 20:
                    ehit = random.choice ([19,19,20,20,20,21,21,22])
                if strength == 21:
                    ehit = random.choice ([20,20,21,21,21,22,22,23])
                if strength == 22:
                    ehit = random.choice ([21,21,22,22,22,23,23,24])
                if strength == 23:
                    ehit = random.choice ([22,22,23,23,23,24,24,25])
                print ("")
                ehit -= defender
                health -= ehit
                print (f"The enemy has done {ehit} damage to you!")
                if health <= 0:
                    print ("You died!")
                    print ("That sucks :(")
                    quit ()
                print (f"You have {health} health left.")
                defense = 0
# this is the second 5 battles with a demon instead of an orc. lines 292 - 601. there's a for loop inside but I dont think I need to explain that
for i in range (5):
    if monster == 0:
        monster += 5
    elif monster == 5:
        monster = 6
    elif monster == 6:
        monster = 7
    elif monster == 7:
        monster = 8
    elif monster == 9:
        monster = 10
    elif monster == 10:
        print ("")
        print ("This is the last of the enemies before the boss!")
        print ("You get to upgrade twice this time!")
    print ("")
    if num == 0:
        monster = random.choice (["demon", "orc"])
    if monster == "demon" and num == 0:
        print ("Looks like your fighting a demon!")
        enemy = random.choice ([35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50])
        est = random.choice ([8,9,10,11,12,13])
        print (f"The demon has {enemy} health!")
        print (f"By the way you have {health} health!")
        num += 1
    if monster == "orc" and num == 0:
        print ("Looks like your fighting a orc!")
        enemy = random.choice ([30,31,32,33,34,35,36,37,38,39,40])
        est = random.choice ([6,7,8,9,10,11])
        print (f"The orc has {enemy} health!")
        print (f"By the way you have {health} health!")
        num += 1
    for i in range (100):
        if num == 1:
            print ("Hey, so you have a few options for what you can do.")
            print ("")
            print ("A. Attack!")
            print ("B. Brace/gather power!")
            if power >= 2:
                print (f"C. Power move(uses 2 power and you currently have {power} power.)")
            print ("")
            question = input ("")
            if question == "A" or question == "a" or question == "A." or question == "a." :
                print ("")
                if strength == 5:
                    hit = random.choice ([4,4,5,5,5,6,6,7])
                if strength == 6:
                    hit = random.choice ([5,5,6,6,6,7,7,8])
                if strength == 7:
                    hit = random.choice ([6,6,7,7,7,8,8,9])
                if strength == 8:
                    hit = random.choice ([7,7,8,8,8,9,9,10])
                if strength == 9:
                    hit = random.choice ([8,8,9,9,9,10,10,11])
                if strength == 10:
                    hit = random.choice ([9,9,10,10,10,11,11,12])
                if strength == 11:
                    hit = random.choice ([10,10,11,11,11,12,12,13])
                if strength == 12:
                    hit = random.choice ([11,11,12,12,12,13,13,14])
                if strength == 13:
                    hit = random.choice ([12,12,13,13,13,14,14,15])
                if strength == 14:
                    hit = random.choice ([13,13,14,14,14,15,15,16])
                if strength == 15:
                    hit = random.choice ([14,14,15,15,15,16,16,17])
                enemy -= hit
                if enemy <= 0:
                    print ("")
                else:
                    print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
            elif question == "B" or question == "b" or question == "B." or question == "b." :
                print ("")
                power += 1
                defense += 1
                print ("Ok, so you are now defending. Cool.")
                print (f"you have {power} power now.")
            elif question == "C" or question == "c" or question == "C." or question == "c." and power >= 2 :
                print ("")
                powerr = random.choice ([4,5,5,5,6,6,7])
                strength += powerr
                if strength == 5:
                    hit = random.choice ([4,4,5,5,5,6,6,7])
                if strength == 6:
                    hit = random.choice ([5,5,6,6,6,7,7,8])
                if strength == 7:
                    hit = random.choice ([6,6,7,7,7,8,8,9])
                if strength == 8:
                    hit = random.choice ([7,7,8,8,8,9,9,10])
                if strength == 9:
                    hit = random.choice ([8,8,9,9,9,10,10,11])
                if strength == 10:
                    hit = random.choice ([9,9,10,10,10,11,11,12])
                if strength == 11:
                    hit = random.choice ([10,10,11,11,11,12,12,13])
                if strength == 12:
                    hit = random.choice ([11,11,12,12,12,13,13,14])
                if strength == 13:
                    hit = random.choice ([12,12,13,13,13,14,14,15])
                if strength == 14:
                    hit = random.choice ([13,13,14,14,14,15,15,16])
                if strength == 15:
                    hit = random.choice ([14,14,15,15,15,16,16,17])
                if strength == 16:
                    hit = random.choice ([15,15,16,16,16,17,17,18])
                if strength == 17:
                    hit = random.choice ([16,16,17,17,17,18,18,19])
                if strength == 18:
                    hit = random.choice ([17,17,18,18,18,19,19,20])
                if strength == 19:
                    hit = random.choice ([18,18,19,19,19,20,20,21])
                if strength == 20:
                    hit = random.choice ([19,19,20,20,20,21,21,22])
                if strength == 21:
                    hit = random.choice ([20,20,21,21,21,22,22,23])
                if strength == 22:
                    hit = random.choice ([21,21,22,22,22,23,23,24])
                if strength == 23:
                    hit = random.choice ([22,22,23,23,23,24,24,25])
                enemy -= hit
                if enemy <= 0:
                    print ("")
                    print (f"You did {hit} damage!")
                else:
                    print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
                strength -= powerr
                power -= 2
            else:
                print ("")
                print ("Hmmm... Looks like you didn't choose one of the options. Just type a or b, not the whole sentence, okay?")
                print ("")
                redoanswer = input ("")
                if redoanswer == "A" or redoanswer == "a" or redoanswer == "A." or redoanswer == "a." :
                    print ("")
                    if strength == 5:
                        hit = random.choice ([4,4,5,5,5,6,6,7])
                    if strength == 6:
                        hit = random.choice ([5,5,6,6,6,7,7,8])
                    if strength == 7:
                        hit = random.choice ([6,6,7,7,7,8,8,9])
                    if strength == 8:
                        hit = random.choice ([7,7,8,8,8,9,9,10])
                    if strength == 9:
                        hit = random.choice ([8,8,9,9,9,10,10,11])
                    if strength == 10:
                        hit = random.choice ([9,9,10,10,10,11,11,12])
                    if strength == 11:
                        hit = random.choice ([10,10,11,11,11,12,12,13])
                    if strength == 12:
                        hit = random.choice ([11,11,12,12,12,13,13,14])
                    if strength == 13:
                        hit = random.choice ([12,12,13,13,13,14,14,15])
                    if strength == 14:
                        hit = random.choice ([13,13,14,14,14,15,15,16])
                    if strength == 15:
                        hit = random.choice ([14,14,15,15,15,16,16,17])
                    enemy -= hit
                    if enemy <= 0:
                        print ("")
                    else:
                        print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
                elif redoanswer == "B" or redoanswer == "b" or redoanswer == "B." or redoanswer == "b." :
                    print ("")
                    power += 1
                    defense += 1
                    print ("Ok, so you are now defending. Cool.")
                    print (f"you have {power} power now.")
                elif redoanswer == "C" or redoanswer == "c" or redoanswer == "C." or redoanswer == "c." and power >= 2 :
                    print ("")
                    powerr = random.choice ([4,5,5,5,6,6,7])
                    strength += powerr
                    if strength == 5:
                        hit = random.choice ([4,4,5,5,5,6,6,7])
                    if strength == 6:
                        hit = random.choice ([5,5,6,6,6,7,7,8])
                    if strength == 7:
                        hit = random.choice ([6,6,7,7,7,8,8,9])
                    if strength == 8:
                        hit = random.choice ([7,7,8,8,8,9,9,10])
                    if strength == 9:
                        hit = random.choice ([8,8,9,9,9,10,10,11])
                    if strength == 10:
                        hit = random.choice ([9,9,10,10,10,11,11,12])
                    if strength == 11:
                        hit = random.choice ([10,10,11,11,11,12,12,13])
                    if strength == 12:
                        hit = random.choice ([11,11,12,12,12,13,13,14])
                    if strength == 13:
                        hit = random.choice ([12,12,13,13,13,14,14,15])
                    if strength == 14:
                        hit = random.choice ([13,13,14,14,14,15,15,16])
                    if strength == 15:
                        hit = random.choice ([14,14,15,15,15,16,16,17])
                    if strength == 16:
                        hit = random.choice ([15,15,16,16,16,17,17,18])
                    if strength == 17:
                        hit = random.choice ([16,16,17,17,17,18,18,19])
                    if strength == 18:
                        hit = random.choice ([17,17,18,18,18,19,19,20])
                    if strength == 19:
                        hit = random.choice ([18,18,19,19,19,20,20,21])
                    if strength == 20:
                        hit = random.choice ([19,19,20,20,20,21,21,22])
                    if strength == 21:
                        hit = random.choice ([20,20,21,21,21,22,22,23])
                    if strength == 22:
                        hit = random.choice ([21,21,22,22,22,23,23,24])
                    if strength == 23:
                        hit = random.choice ([22,22,23,23,23,24,24,25])
                    enemy -= hit
                    if enemy <= 0:
                        print ("")
                        print (f"You did {hit} damage!")
                    else:
                        print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
                    strength -= powerr
                    power -= 2
                else:
                    print ("")
                    print ("OK!!! STOP BEING ANNOYING!!! JUST CHOOSE SOMETHING!!! ACTUALLY, SCRATCH THAT! LEAVE ME ALONE AND TRY AGAIN WHEN YOU CAN HANDLE THIS!!!")
                    quit ()
            time.sleep(2)
            if enemy <= 0:
                num = 0
                power = 0
                print ("You beat the enemy!")
                print (f"You still have {health} health!")
                print ("Do you want to put your upgrade points into health (fully heals you and gives +5 max. health) or strength (increases damage)?")
                print ("")
                question = input ("")
                if question == "a" or question == "A" or question == "a." or question == "A." or question == "health" or question == "Health" or question == "heal" or question == "Heal" or question == "Max. health" or question == "Max health" or question == "max. health" or question == "max health" or question == "Max. Health" or question == "Max Health":
                    print ("")
                    max_health += 5
                    health = max_health
                    print (f"Ok! now you have {health} health!")
                elif question == "b" or question == "B" or question == "b." or question == "B." or question == "strength" or question == "Strength" or question == "damage" or question == "Damage" or question == "increase damage" or question == "Increase damage" or question == "Increase Damage":
                    print ("")
                    strength += 1
                    print ("You have increased your damage!")
                
                else: 
                    print ("Hmmm... I'm not sure what you just said. Please just say something like 'health' or 'strength' or 'a' or 'b' or something along those lines.")
                    print ("")
                    redoanswer = input("")
                    if redoanswer == "a" or redoanswer == "A" or redoanswer == "a." or redoanswer == "A." or redoanswer == "health" or redoanswer == "Health" or redoanswer == "heal" or redoanswer == "Heal" or redoanswer == "Max. health" or redoanswer == "Max health" or redoanswer == "max. health" or redoanswer == "max health" or redoanswer == "Max. Health" or redoanswer == "Max Health":
                        print ("")
                        max_health += 5
                        health = max_health
                        print (f"Ok! now you have {health} health!")
                    if redoanswer == "b" or redoanswer == "B" or redoanswer == "b." or redoanswer == "B." or redoanswer == "strength" or redoanswer == "Strength" or redoanswer == "damage" or redoanswer == "Damage" or redoanswer == "increase damage" or redoanswer == "Increase damage" or redoanswer == "Increase Damage":
                        print ("")
                        strength += 1
                        print ("You have increased your damage!")
                if monster == 10:
                    print ("")
                    print ("You get another choice!")
                    print (f"You have {health} health!")
                    print ("Do you want to put your upgrade points into health (fully heals you and gives +5 max. health) or strength (increases damage)?")
                    print ("")
                    question = input ("")
                    if question == "a" or question == "A" or question == "a." or question == "A." or question == "health" or question == "Health" or question == "heal" or question == "Heal" or question == "Max. health" or question == "Max health" or question == "max. health" or question == "max health" or question == "Max. Health" or question == "Max Health":
                        print ("")
                        max_health += 5
                        health = max_health
                        print (f"Ok! now you have {health} health!")
                        print ("Onto the boss!")
                    elif question == "b" or question == "B" or question == "b." or question == "B." or question == "strength" or question == "Strength" or question == "damage" or question == "Damage" or question == "increase damage" or question == "Increase damage" or question == "Increase Damage":
                        print ("")
                        strength += 1
                        print ("You have increased your damage!")
                        print ("Onto the boss")
                    
                    else: 
                        print ("Hmmm... I'm not sure what you just said. Please just say something like 'health' or 'strength' or 'a' or 'b' or something along those lines.")
                        print ("")
                        redoanswer = input("")
                        if redoanswer == "a" or redoanswer == "A" or redoanswer == "a." or redoanswer == "A." or redoanswer == "health" or redoanswer == "Health" or redoanswer == "heal" or redoanswer == "Heal" or redoanswer == "Max. health" or redoanswer == "Max health" or redoanswer == "max. health" or redoanswer == "max health" or redoanswer == "Max. Health" or redoanswer == "Max Health":
                            print ("")
                            max_health += 5
                            health = max_health
                            print (f"Ok! now you have {health} health!")
                            print ("Onto the boss")
                        if redoanswer == "b" or redoanswer == "B" or redoanswer == "b." or redoanswer == "B." or redoanswer == "strength" or redoanswer == "Strength" or redoanswer == "damage" or redoanswer == "Damage" or redoanswer == "increase damage" or redoanswer == "Increase damage" or redoanswer == "Increase Damage":
                            print ("")
                            strength += 1
                            print ("You have increased your damage!")
                            print ("Onto the boss")
                else:
                    print ("Onto the next battle!")
            else:
                print ("")
                print ("Ok. Time for the enemy to hit you!")
                if defense == 1:
                    defender = random.choice ([1,2,2,3,3,4])
                if strength == 5:
                    ehit = random.choice ([4,4,5,5,5,6,6,7])
                if strength == 6:
                    ehit = random.choice ([5,5,6,6,6,7,7,8])
                if strength == 7:
                    ehit = random.choice ([6,6,7,7,7,8,8,9])
                if strength == 8:
                    ehit = random.choice ([7,7,8,8,8,9,9,10])
                if strength == 9:
                    ehit = random.choice ([8,8,9,9,9,10,10,11])
                if strength == 10:
                    ehit = random.choice ([9,9,10,10,10,11,11,12])
                if strength == 11:
                    ehit = random.choice ([10,10,11,11,11,12,12,13])
                if strength == 12:
                    ehit = random.choice ([11,11,12,12,12,13,13,14])
                if strength == 13:
                    ehit = random.choice ([12,12,13,13,13,14,14,15])
                if strength == 14:
                    ehit = random.choice ([13,13,14,14,14,15,15,16])
                if strength == 15:
                    ehit = random.choice ([14,14,15,15,15,16,16,17])
                print ("")
                ehit -= defender
                health -= ehit
                print (f"The enemy has done {ehit} damage to you!")
                if health <= 0:
                    print ("You died!")
                    print ("That sucks :(")
                    quit ()
                print (f"You have {health} health left.")
                defense = 0
print ("")
time.sleep(2)
print ("The boss battle is upon us!")
print ("")
print ("Here he is! Oof he is a beast!")
enemy = random.choice ([60,61,62,63,64,65,66,67,68,69,70])
est = random.choice ([13,14,15,16,17,18])
print (f"The orc has {enemy} health!")
print (f"By the way you have {health} health!")
# this is the boss fight. lines 612 - 830. 
for i in range (100):
    if boss == 0:
        print ("")
    else:
        num = 1
        if num == 1:
            print ("Hey, so you have a few options for what you can do.")
            print ("")
            print ("A. Attack!")
            print ("B. Brace/gather power!")
            if power >= 2:
                print (f"C. Power move(uses 2 power and you currently have {power} power.)")
            print ("")
            question = input ("")
            if question == "A" or question == "a" or question == "A." or question == "a." :
                print ("")
                if strength == 5:
                    hit = random.choice ([4,4,5,5,5,6,6,7])
                if strength == 6:
                    hit = random.choice ([5,5,6,6,6,7,7,8])
                if strength == 7:
                    hit = random.choice ([6,6,7,7,7,8,8,9])
                if strength == 8:
                    hit = random.choice ([7,7,8,8,8,9,9,10])
                if strength == 9:
                    hit = random.choice ([8,8,9,9,9,10,10,11])
                if strength == 10:
                    hit = random.choice ([9,9,10,10,10,11,11,12])
                if strength == 11:
                    hit = random.choice ([10,10,11,11,11,12,12,13])
                if strength == 12:
                    hit = random.choice ([11,11,12,12,12,13,13,14])
                if strength == 13:
                    hit = random.choice ([12,12,13,13,13,14,14,15])
                if strength == 14:
                    hit = random.choice ([13,13,14,14,14,15,15,16])
                if strength == 15:
                    hit = random.choice ([14,14,15,15,15,16,16,17])
                enemy -= hit
                if enemy <= 0:
                    print ("")
                else:
                    print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
            elif question == "B" or question == "b" or question == "B." or question == "b." :
                print ("")
                power += 1
                defense += 1
                print ("Ok, so you are now defending. Cool.")
                print (f"you have {power} power now.")
            elif question == "C" or question == "c" or question == "C." or question == "c." and power >= 2 :
                print ("")
                powerr = random.choice ([4,5,5,5,6,6,7])
                strength += powerr
                if strength == 5:
                    hit = random.choice ([4,4,5,5,5,6,6,7])
                if strength == 6:
                    hit = random.choice ([5,5,6,6,6,7,7,8])
                if strength == 7:
                    hit = random.choice ([6,6,7,7,7,8,8,9])
                if strength == 8:
                    hit = random.choice ([7,7,8,8,8,9,9,10])
                if strength == 9:
                    hit = random.choice ([8,8,9,9,9,10,10,11])
                if strength == 10:
                    hit = random.choice ([9,9,10,10,10,11,11,12])
                if strength == 11:
                    hit = random.choice ([10,10,11,11,11,12,12,13])
                if strength == 12:
                    hit = random.choice ([11,11,12,12,12,13,13,14])
                if strength == 13:
                    hit = random.choice ([12,12,13,13,13,14,14,15])
                if strength == 14:
                    hit = random.choice ([13,13,14,14,14,15,15,16])
                if strength == 15:
                    hit = random.choice ([14,14,15,15,15,16,16,17])
                if strength == 16:
                    hit = random.choice ([15,15,16,16,16,17,17,18])
                if strength == 17:
                    hit = random.choice ([16,16,17,17,17,18,18,19])
                if strength == 18:
                    hit = random.choice ([17,17,18,18,18,19,19,20])
                if strength == 19:
                    hit = random.choice ([18,18,19,19,19,20,20,21])
                if strength == 20:
                    hit = random.choice ([19,19,20,20,20,21,21,22])
                if strength == 21:
                    hit = random.choice ([20,20,21,21,21,22,22,23])
                if strength == 22:
                    hit = random.choice ([21,21,22,22,22,23,23,24])
                if strength == 23:
                    hit = random.choice ([22,22,23,23,23,24,24,25])
                enemy -= hit
                if enemy <= 0:
                    print ("")
                    print (f"You did {hit} damage!")
                else:
                    print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
                strength -= powerr
                power -= 2
            else:
                print ("")
                print ("Hmmm... Looks like you didn't choose one of the options. Just type a or b, not the whole sentence, okay?")
                print ("")
                redoanswer = input ("")
                if redoanswer == "A" or redoanswer == "a" or redoanswer == "A." or redoanswer == "a." :
                    print ("")
                    if strength == 5:
                        hit = random.choice ([4,4,5,5,5,6,6,7])
                    if strength == 6:
                        hit = random.choice ([5,5,6,6,6,7,7,8])
                    if strength == 7:
                        hit = random.choice ([6,6,7,7,7,8,8,9])
                    if strength == 8:
                        hit = random.choice ([7,7,8,8,8,9,9,10])
                    if strength == 9:
                        hit = random.choice ([8,8,9,9,9,10,10,11])
                    if strength == 10:
                        hit = random.choice ([9,9,10,10,10,11,11,12])
                    if strength == 11:
                        hit = random.choice ([10,10,11,11,11,12,12,13])
                    if strength == 12:
                        hit = random.choice ([11,11,12,12,12,13,13,14])
                    if strength == 13:
                        hit = random.choice ([12,12,13,13,13,14,14,15])
                    if strength == 14:
                        hit = random.choice ([13,13,14,14,14,15,15,16])
                    if strength == 15:
                        hit = random.choice ([14,14,15,15,15,16,16,17])
                    enemy -= hit
                    if enemy <= 0:
                        print ("")
                    else:
                        print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
                elif redoanswer == "B" or redoanswer == "b" or redoanswer == "B." or redoanswer == "b." :
                    print ("")
                    power += 1
                    defense += 1
                    print ("Ok, so you are now defending. Cool.")
                    print (f"you have {power} power now.")
                elif redoanswer == "C" or redoanswer == "c" or redoanswer == "C." or redoanswer == "c." and power >= 2 :
                    print ("")
                    powerr = random.choice ([4,5,5,5,6,6,7])
                    strength += powerr
                    if strength == 5:
                        hit = random.choice ([4,4,5,5,5,6,6,7])
                    if strength == 6:
                        hit = random.choice ([5,5,6,6,6,7,7,8])
                    if strength == 7:
                        hit = random.choice ([6,6,7,7,7,8,8,9])
                    if strength == 8:
                        hit = random.choice ([7,7,8,8,8,9,9,10])
                    if strength == 9:
                        hit = random.choice ([8,8,9,9,9,10,10,11])
                    if strength == 10:
                        hit = random.choice ([9,9,10,10,10,11,11,12])
                    if strength == 11:
                        hit = random.choice ([10,10,11,11,11,12,12,13])
                    if strength == 12:
                        hit = random.choice ([11,11,12,12,12,13,13,14])
                    if strength == 13:
                        hit = random.choice ([12,12,13,13,13,14,14,15])
                    if strength == 14:
                        hit = random.choice ([13,13,14,14,14,15,15,16])
                    if strength == 15:
                        hit = random.choice ([14,14,15,15,15,16,16,17])
                    if strength == 16:
                        hit = random.choice ([15,15,16,16,16,17,17,18])
                    if strength == 17:
                        hit = random.choice ([16,16,17,17,17,18,18,19])
                    if strength == 18:
                        hit = random.choice ([17,17,18,18,18,19,19,20])
                    if strength == 19:
                        hit = random.choice ([18,18,19,19,19,20,20,21])
                    if strength == 20:
                        hit = random.choice ([19,19,20,20,20,21,21,22])
                    if strength == 21:
                        hit = random.choice ([20,20,21,21,21,22,22,23])
                    if strength == 22:
                        hit = random.choice ([21,21,22,22,22,23,23,24])
                    if strength == 23:
                        hit = random.choice ([22,22,23,23,23,24,24,25])
                    enemy -= hit
                    if enemy <= 0:
                        print ("")
                        print (f"You did {hit} damage!")
                    else:
                        print (f"You did {hit} damage! They only have {enemy} health to go before they are defeated!")
                    strength -= powerr
                    power -= 2
                else:
                    print ("")
                    print ("OK!!! STOP BEING ANNOYING!!! JUST CHOOSE SOMETHING!!! ACTUALLY, SCRATCH THAT! LEAVE ME ALONE AND TRY AGAIN WHEN YOU CAN HANDLE THIS!!!")
                    quit ()
            time.sleep(2)
            if enemy <= 0:
                boss = 0
            else:
                print ("")
                print ("Ok. Time for the enemy to hit you!")
                if defense == 1:
                    defender = random.choice ([2,3,3,4,4,5])
                if strength == 5:
                    ehit = random.choice ([4,4,5,5,5,6,6,7])
                if strength == 6:
                    ehit = random.choice ([5,5,6,6,6,7,7,8])
                if strength == 7:
                    ehit = random.choice ([6,6,7,7,7,8,8,9])
                if strength == 8:
                    ehit = random.choice ([7,7,8,8,8,9,9,10])
                if strength == 9:
                    ehit = random.choice ([8,8,9,9,9,10,10,11])
                if strength == 10:
                    ehit = random.choice ([9,9,10,10,10,11,11,12])
                if strength == 11:
                    ehit = random.choice ([10,10,11,11,11,12,12,13])
                if strength == 12:
                    ehit = random.choice ([11,11,12,12,12,13,13,14])
                if strength == 13:
                    ehit = random.choice ([12,12,13,13,13,14,14,15])
                if strength == 14:
                    ehit = random.choice ([13,13,14,14,14,15,15,16])
                if strength == 15:
                    ehit = random.choice ([14,14,15,15,15,16,16,17])
                if strength == 16:
                    ehit = random.choice ([15,15,16,16,16,17,17,18])
                if strength == 17:
                    ehit = random.choice ([16,16,17,17,17,18,18,19])
                if strength == 18:
                    ehit = random.choice ([17,17,18,18,18,19,19,20])
                if strength == 19:
                    ehit = random.choice ([18,18,19,19,19,20,20,21])
                if strength == 20:
                    ehit = random.choice ([19,19,20,20,20,21,21,22])
                if strength == 21:
                    ehit = random.choice ([20,20,21,21,21,22,22,23])
                if strength == 22:
                    ehit = random.choice ([21,21,22,22,22,23,23,24])
                if strength == 23:
                    ehit = random.choice ([22,22,23,23,23,24,24,25])
                print ("")
                ehit -= defender
                health -= ehit
                print (f"The enemy has done {ehit} damage to you!")
                if health <= 0:
                    print ("You died!")
                    print ("That sucks :(")
                    print ("Right at the end too.")
                    print ("So close.")
                    quit ()
                print (f"You have {health} health left.")
                defense = 0
print ("You beat the boss!")
print ("You won the game user!")
print ("Congrats!")
print ("Yay :)")
quit ()