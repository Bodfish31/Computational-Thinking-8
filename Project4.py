import time
import random
health = 50
strength = 5
num = 0
enemy = 0
power = 0
print ("Hello user! Today you will be playing a turn-based game!")
print ("")
print ("In a land called... sigh.")
print ("I dont feel like doing world building today.")
print ("In fact, I dont feel like making any storyline.")
print ("So, lets thrown interesting stories to the wind!")
print ("")
print ("Ok, so you are in a dungeon bla bla bla defeat the monsters.")
print ("You are walking and boom! A monster is in your path.")
print ("Engage the enemy!")
time.sleep(2)
for i in range (100):
    print ("")
    if num == 0:
        monster = random.choice (["goblin", "orc"])
    if monster == "goblin" and num == 0:
        print ("Looks like your fighting a goblin!")
        enemy = random.choice ([25,26,27,28,29,30,31,32,33,34,35])
        print (f"The goblin has {enemy} health!")
        print (f"By the way you have {health} health!")
        num += 1
    if monster == "goblin" and num == 0:
        print ("Looks like your fighting a orc!")
        enemy = random.choice ([30,31,32,33,34,35,36,37,38,39,40])
        print (f"The goblin has {enemy} health!")
        print (f"By the way you have {health} health!")
        num += 1
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
            hit = random.choice ([14,14,15,15,15,16,16,17]  )
        enemy -= hit
        print (f"You did {hit} damage! They only have {enemy} health left!")
    elif question == "B" or question == "b" or question == "B." or question == "b." :
        print ("")
    elif question == "C" or question == "c" or question == "C." or question == "c." :
        print ("")
    else:
        print ("")
        print ("Hmmm... Looks like you didn't choose one of the options. Just type a, b, or c, not the whole sentence, okay?")
        print ("")
        redoanswer = input ("")
        if redoanswer == "A" or redoanswer == "a" or redoanswer == "A." or redoanswer == "a." :
            print ("")
        elif redoanswer == "B" or redoanswer == "b" or redoanswer == "B." or redoanswer == "b." :
            print ("")
        elif redoanswer == "C" or redoanswer == "c" or redoanswer == "C." or redoanswer == "c." :
            print ("")
        else:
            print ("")
            print ("OK!!! STOP BEING ANNOYING!!! JUST CHOOSE SOMETHING!!! ACTUALLY, SCRATCH THAT! LEAVE ME ALONE AND TRY AGAIN WHEN YOU CAN HANDLE THIS!!!")

    
