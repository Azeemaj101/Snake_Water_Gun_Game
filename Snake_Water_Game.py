import random
import os
# S For Snake, W For Water, G For Gun
lst = ['s', 'w', 'g']

# Variables
Chance = 10
No_Chance = 0
Computer_Points = 0
User_Points = 0

_input = {"s": "Snake", "g": "Gun", "w": "Water"}

print("\033[32m\033[01m\t\t\t\t\t*****Welcome To Snake Water Gun Game*****")
_Name = input("Please Enter Your Name\n")

# While loop Run Till 10
while No_Chance < Chance:
    # Use Random Module
    Computer = random.choice(lst)
    user = input("Enter S For Sanke \nEnter W For Water \nEnter G For Gun\n").lower()
    if user == Computer:
        print("Tie Both 0 Points")
    elif user == 's' and Computer == 'g':
        Computer_Points = Computer_Points + 1
        print("Computer Wins 1 Point")
        print(f"Your Guess {_input[user]} & Computer Guess {_input[Computer]}")
        print(f"Points: \n{_Name} = {User_Points} \nComputer = {Computer_Points}")
    elif user == 's' and Computer == 'w':
        User_Points = User_Points + 1
        print(f"{_Name} Wins 1 Point")
        print(f"Your Guess {_input[user]} & Computer Guess {_input[Computer]}")
        print(f"Points: \n{_Name} = {User_Points} \nComputer = {Computer_Points}")
    elif user == 'w' and Computer == 's':
        Computer_Points = Computer_Points + 1
        print("Computer Wins 1 Point")
        print(f"Your Guess {_input[user]} & Computer Guess {_input[Computer]}")
        print(f"Points: \n{_Name} = {User_Points} \nComputer = {Computer_Points}")
    elif user == 'w' and Computer == 'g':
        User_Points = User_Points + 1
        print(f"{_Name} Wins 1 Point")
        print(f"Your Guess {_input[user]} & Computer Guess {_input[Computer]}")
        print(f"Points: \n{_Name} = {User_Points} \nComputer = {Computer_Points}")
    elif user == 'g' and Computer == 's':
        User_Points = User_Points + 1
        print(f"{_Name} Wins 1 Point")
        print(f"Your Guess {_input[user]} & Computer Guess {_input[Computer]}")
        print(f"Points: \n{_Name} = {User_Points} \nComputer = {Computer_Points}")
    elif user == 'g' and Computer == 'w':
        Computer_Points = Computer_Points + 1
        print("Computer Wins 1 Point")
        print(f"Your Guess {_input[user]} & Computer Guess {_input[Computer]}")
        print(f"Points: \n{_Name} = {User_Points} \nComputer = {Computer_Points}")
    else:
        print("Wrong Key")
        os.system("pause")
    No_Chance = No_Chance + 1
print("\n\n\n\t\t\t\t\033[31m*********Game Over*********\n\n\n")
print(f"Points: \n{_Name} = {User_Points} \nComputer = {Computer_Points}")
if User_Points > Computer_Points:
    print(f"Congratulation {_Name} Won The Game")
elif User_Points < Computer_Points:
    print("Game Over Computer Won")
elif User_Points == Computer_Points:
    print("Game Tie")
