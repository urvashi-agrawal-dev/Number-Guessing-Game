#Number guessing game
import random
import math
from_guess=int(input("Enter a from no"))
to_guess=int(input("Enter a to no"))
x=random.randint(from_guess,to_guess)
print("\n\tYou've only ", 
    round((to_guess - from_guess + 1) ** 0.5),
    " chances to guess the integer!\n")
c=0
while c<((to_guess - from_guess + 1) ** 0.5):
    c+=1
    guess=int(input("Guess any no in the range"))
    if x==guess:
        print("\n\t u've guessed it",c,"times")
        break
    elif x>guess:
        print("u've guessed the too small int")
    elif x<guess:
        print ("u've guessed the too big int")
if c>=((to_guess - from_guess + 1) ** 0.5):
    print("\n\t the no is %d" %x)
    print("\U0001F61E u loose")

