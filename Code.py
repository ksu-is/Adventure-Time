from turtle import left


name = input("Enter your name: ")

print("Welcome", name, "to your Starbucks Adventure. You stayed up all night studying for your exam and need a boost for the day. \n Only problem is you start class in 30 minutes. Find your way to Starbucks and secure your drink before class starts!")
time = 30 
while True:
    q1 = input ("On your way to campus, a tree fell. To try to get around the fall of the tree and potential traffic, \n you can go left or right? (pick one: left/right) ")
    if q1.lower() == "left":
        q2 = input("After that almost trafffic jam, you park your car at the Central Deck and begin your walk to Starbucks. On that walk, you see a friend that you haven't \n seen in while. This causes you guys to catch up and this goes on for about 5 minutes. You look at the time and notice you need to head to Starbuck soon so you're not late for class. Do you ask your friend to walk with you or just leave them behind? (pick one: walk/leave)")
        if q2.lower() == "walk":
            q3 = ("You have just been given 5 more minutes for bringing your friend along. Now, you can talk to them along the way and even make plans to hang out later. WOAH, WOAH, your friend has now fallen, do you help them or leave them behind? (pick one: stay/leave)")
            if q3.lower() == "leave":
                time += 5
                print("You are now walking to Starbucks by yourself so you listen to music to keep you company. Make sure to look at the time along your walk. ")
                break
            elif q3 == "walk": 
                print("You are now walking to Starbucks by yourself so you listen to music to keep you company. Make sure to look at the time along your walk.")
                break
        else:
           print("Please enter a valid answer.")
      elif q2.lower() == "leave":
        q4 = input("For leaving, you gained 10 minutes. You find a secret shortcut that can save you 7 mintues, do you take it? (pick one: yes/no) ")
        if q4.lower() == "yes":
            time +=17
            print("Good option!, you have just saved 7 miuntes. You also gain 10 miunutes from earlier and get to Starbucks faster.")
            break
        elif q4.lower() == "no":
            time +=10
            print("You have gained 10 minutes for your travel.")
            break
        else:
            print("Please enter a valid answer.")
      else:
        print("Please enter a valid answer.")
    elif :