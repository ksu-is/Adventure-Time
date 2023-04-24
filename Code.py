from turtle import left


l1 = "left"
r1 = "right"
l2 = "talk"
r2 = "ignore"





name = input("Enter your name: ")
print("Welcome " + name +  " The Game: Starbucks Adventure Time!")

print("Welcome", name, "to your Starbucks Adventure. You stayed up all night studying for your exam and need a boost for the day. \n Only problem is you start class in 30 minutes. Find your way to Starbucks and secure your drink before class starts!")
time = 30 
while True:
    q1 = input ("A tree fell. Where are you going to go? (left/right)")
    if q1.lower() == l1.lower():
        q2 = input("You get stopped by a professor. What will you do? (talk/ingore)")
    elif q1 == r2.lower():


