from turtle import left
from turtle import right

name = input("Enter your name: ")

print("Welcome", name, "to your Starbucks Adventure. You stayed up all night studying for your exam and need a boost for the day.\nOnly problem is you start class in 45 minutes. Find your way to Starbucks and secure your drink before class starts!")
time = 45 
while True:
    q1 = input ("On your way to campus, a tree fell. To try to get around the fall of the tree and potential traffic, you can go left or right? (pick one: left/right) ")
    if q1.lower() == "left":
        q2 = input("After that almost traffic jam, you park your car at the Central Deck and begin your walk to Starbucks. On that walk, you see a friend that you haven't seen in while.\nThis causes you guys to catch up and this goes on for about 5 minutes. You look at the time and notice you need to head to Starbuck soon so you're not late for class.\nDo you ask your friend to walk with you or just continue walking? (pick one: ask/continue)")
        if q2.lower() == "ask":
            q3 = ("You have just been given 5 more minutes for bringing your friend along. Now, you can talk to them along the way and even make plans to hang out later.\nWOAH, WOAH, your friend has now fallen, do you help them or leave them behind? (pick one: stay/leave)")
            if q3.lower() == "leave":
                time +=5
                print("You are now walking to Starbucks by yourself so you listen to music to keep you company. Make sure to look at the time along your walk. ")
                break
            elif q3 == "walk": 
                time -=10
                print("You are now helping your friend to make sure they are okay. Your time is now running out. Head to Starbucks soon so you can get to class on time.")
                break
            else:
                print("Please enter a valid answer.")
        elif q2.lower() == "continue":
            q4 = input("For leaving, you find a secret shortcut that can save you 7 mintues, do you take it? (pick one: yes/no) ")
            if q4.lower() == "yes":
                time +=7
                print("Good option!, you have just saved 7 miuntes and can now get to Starbucks faster.")
                print("Nice moves, you made  it, get your drink and head to class!")
                break
            elif q4.lower() == "no":
                time -=10
                print("You have lost 10 minutes for your travel. Hurry up so you can get to class before time runs out.")
                break
            else:
                print("Please enter a valid answer.")
        else:
            print("Please enter a valid answer.")
    elif q1.lower() == "right":
        q5 = input("After that almost traffic jam, you park your car at the Central Deck and begin your walk to Starbucks. On this walk you get stopped by a\nvideographer asking you to be in their Youtube video. You can decide to be in the Youtube video or not. (pick one: yes/no) ")
        if q5.lower()== "yes":
            q6 = input("Because you chose to be in the video, you lost five minutes, but they offer you to stay longer for another scene. Do you stay or leave? (pick one: stay/leave)")
            if q6.lower() == "stay":
                time -=5
                print("Because you chose to stay, you lost another three minutes, but you got two nice scenes in the video :) ")
                break
            elif q6.lower() == "leave":
                time +=2
                print("Because you decided to leave you only lost 3 minutes of time instead of 5.")
                break
            else: 
                print("Please enter a valid answer.")
        elif q5.lower()== "no":
            q7 = input("You chose not to be in the video and instead a friend rides by on a scooter and asks to take you to Starbucks. Do you take the ride or continue walk? (pick one: ride/walk)")
            if q7.lower()== "ride":
                time +=7 
                print("Because you chose to ride, you saved 7 minutes and arrive at Starbucks early!")
                break
            elif q7.lower() == "walk":
                time -=10
                print("Because you decided to walk, you lost 10 more minutes and didn't make it to Starbucks. Now you're late for class :( )")
                break
            else:
                print("Please enter a valid answer.")
        else:
            print("Please enter a valid answer.")
    else:
        print("Please enter a valid answer.")

def time_calculate():
    if time > 9:
        end_game = print("Wow", name, ", you got your Starbucks and made it back to class a few minutes early! :)")
        quit()
    elif time < 1:
        end_game = print("Uh oh, you're out of time, " , name, ". You weren't able to get your Starbucks drink and are now late for class. :(")
        quit()
    else:
        end_game = print("You made it right on time to class with your Starbucks drink. Next time, you should ")


time_calculate()