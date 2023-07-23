##Guess the number game
##topics: random module,for loop,f string
import random
number=random.randint(1,10)
for i in range(0,3):
    user=int(input("guess the number\n"))
    if user==number:
        print('Right guess\n')
        print(f'the number is:{number}')
if user!=number:
    print(f"Wrong guess the number is {number}")

