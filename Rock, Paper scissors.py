# 5 point rock paper scissor game
import random

options = ["rock", "paper", "scissor"]

me = 0
computer = 0
for i in range(5):
    comp = random.choice(options)
    answer = input("please enter a choice: rock, paper or scissor")
    if answer == comp:
        print("it is a tie")
    elif answer == "rock" and comp == "paper":
        print ("you get a point")
        me += 1
    elif answer == "rock" and comp == "scissor":
        print ("computer gets a point")
        computer += 1
    elif answer == "paper" and comp == "scissor":
        print ("you get a point")
        me += 1
    elif answer == "paper" and comp == "rock":
        print ("computer gets a point")
        computer += 1
    elif answer == "scissor" and comp == "rock":
        print ("computer gets a point")
        computer += 1
    elif answer == "scissor" and comp == "paper":
        print ("you get a point")
        me += 1
    else:
        print ("please enter a valid choice: rock, paper or scissor")

if me > computer:
    print("you win!")
elif me < computer:
    print ("you lose")
else:
    print("it's a tie")
