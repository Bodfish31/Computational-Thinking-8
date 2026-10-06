place = input ("You wake up. Where will you go today?\n")
if place == "stay home" or place == "home" or place == "Home" or place == "Stay home":
    print ("Ok, so you want a slow start. lets go.")
    input ("")
    wake_up = input ("Its 7 am. want to sleep in or get out of bed?\n")
    if wake_up == "sleep in" or wake_up == "Sleep in" or wake_up == "sleep":
            print ("Alright sleepy-head!")
elif place == "go to school" or place == "school" or place == "Go to school" or place == "School":
    print ("so studius! Well, lets get started.")
    input ("")

else:
    print ("Hmmmm... instead, try to pick either staying home or going to school.")