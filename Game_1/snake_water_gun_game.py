'''
snake = 1
water = -1
gun = 0

'''
import random
computer = random.choice([1,-1,0])
youstr = input("enter your choice: ") 
yourdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}
you = yourdict[youstr]

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer == you):
    print("it's a draw")
else:
    if(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win!")
    elif(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 0 and you == 1):
        print("you lose!")
    elif(computer == 0 and you == -1):
        print("you win!")
    else:
        print("something went wrong")
