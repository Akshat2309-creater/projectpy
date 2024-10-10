# project on a perfect guess game

# import random to generate the random number

import random


n = random.randint(1,100)  # random number from 1 to 100

a = -1                     # a is -1 which means not equal to n

guesses = 0                #intialise guesses value to 0

while(a != n):
    
    guesses+=1              # increment the guesses
    
    a = int(input("Enter the number:")) # number enter by a user
    
    if(a > n):
         
         print("Lower number please")
    
    else:
        
         print("Higher number please")

print(f"You guess the number {n} correctly in {guesses} attempt") # f-string
    