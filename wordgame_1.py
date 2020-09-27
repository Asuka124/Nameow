""" ---------Python Day2---------- """
import random

counts = 3
answer = random.randint(0, 42)
while (counts > 0):
    temp = input("Rewards if you know the random number:")
    guess = int(temp)
    if guess == answer:
        print("Correct")
        print("Here is the rewards: ❤")
        break
    else:   
        print("I told you")
        if guess < answer:
            print("bigger")
        else:
            print("smaller")
        counts =counts - 1
print("you are free to go. The answer is " + str(answer))
 
