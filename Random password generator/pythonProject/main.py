##Random password generator
##topics: random module,joining string
import random
passlen=int(input("Enter password length\n"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
sample="".join(random.sample(s,passlen))
print(sample)
