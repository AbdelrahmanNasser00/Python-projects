##Dice roll simulator
##topics: random module,looping,if-else
import random
while True:
    print("choose: 1-roll the dice       2-Exit")
    user=int(input("what you want to do?!\n"))
    if user==1:
        number=random.randint(1,6)
        print(number)
    else:
        break
