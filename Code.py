from turtle import left


l1 = "left"
r1 = "right"
l2 = "talk"
r2 = "ignore"

name = input("Enter your name: ")

print("Welcome", name, "to your Starbucks Adventure. You stayed up all night studying for your exam and need a boost for the day. \n Only problem is you start class in 30 minutes. Find your way to Starbucks and secure your drink before class starts!")
time = 30 
while True:
    q1 = input ("On your way to campus, a tree fell. To try to get around the fall of the tree and potential traffic, you can go left or right? (pick one: left/right)")
    if q1.lower() == l1.lower():
        q2 = input("After that almost trafffic jam, you park your car at the Central Deck and begin your walk to Starbucks. On that walk, you see a friend that you haven't seen in while.\n This causes you guys to catch up and this goes on for about 5 minutes. You look at the time and notice you need to head to Starbuck soon so you're not late for class. Do you ask your friend to walk with you or just leave them behind? (pick one: walk/leave)")
        q2 = input("You get stopped by a professor. You start catch up and seeing what's new. This goes on for about 5 minutes. You look at the time and notice you need to go to class NOW! What will you do? (pick one: talk/ingore)")
    elif q1 == r2.lower(): 
        print ( )
    else:
           print("Please enter a valid answer")

