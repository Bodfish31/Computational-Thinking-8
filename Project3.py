river = 0
thunder = 0
wind = 0
shadow = 0
sky = 0
star = 0
pet = 0
rogue = 0

def question2 ():
    print ("")


print ("Hello user! I would like you to imagine you are a cat...")
print ("But not just any cat.")
print ("You are a cat in the universe of Warriors!")
print ("What would be your name in this universe. you dont need to be a warrior!")
print ("")
name = input ("")
print ("")
print (f"So, answer the following questions as you, but imagining you, as the cat name {name}!")
print ("")
print ("A. I like being solo, not relying on others.")
print ("B. I feel most comfortable in a group.")
print ("")
answer_1 = input ("")
if answer_1 == "A" or answer_1 == "a" or answer_1 == "A." or answer_1 == "a." :
    rogue += 2
    pet += 1
    star -= 0.5
    shadow -= 0.5
    sky -= .5
    thunder -= 1
    wind -= .5
elif answer_1 == "B" or answer_1 == "b" or answer_1 == "B." or answer_1 == "b." :
    rogue -= 1.5
    star += .5
    sky += .5
    shadow += .5
    wind += .5
    thunder += 1
    river += .5
    pet -= .5
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
    elif redoanswer1 == "B" or redoanswer1 == "b" or redoanswer1 == "B." or redoanswer1 == "b." :
        rogue -= 1.5
        star += .5
        sky += .5
        shadow += .5
        wind += .5
        thunder += 1
        river += .5
        pet -= .5
question2 ()