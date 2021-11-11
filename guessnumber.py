# program for guessing number 

import random

print( " Hello welcome to random gate")
number = int(input("enter the number"))
print( " entered number ", number)
rand = random.randint(1,10);
while(number != rand):
    number = int(input("enter the number"))
    rand = random.randint(1,10);
    if( rand == number):
        print( " woo hooo your guess correct")
    else:
        print( " Try again ...")
