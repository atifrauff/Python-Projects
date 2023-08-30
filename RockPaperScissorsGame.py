 # importing random module to use later
import random

# creating a function which will check whether the computer wins or user
def check(bot, choice):
    if bot == choice:
        return 0
    elif bot == 1 and choice == 2:
        return 1
    elif bot == 1 and choice == 3:
        return -1
    elif bot == 2 and choice == 1:
        return -1
    elif bot == 2 and choice == 3:
        return  1
    elif bot == 3 and choice == 1:
        return 1
    elif bot == 3 and choice == 2:
        return -1

# printing the welcome line for user
print("Welcome to our first ever classic game of 'Rock, Paper, Scissors'")
print("The game will continue until you enter any random number except (1-3).")

# as for as the program is true, the game will continue to run
while True:
    choice = input("""\nWhat do you want to choose:
    1 for 'Rock'
    2 for 'Paper'
    3 for 'Scissors'
    Enter your choice:  """)
    if choice == '1':
        print(f"\nThe choice of user is 'Rock'")
    elif choice == '2':
        print(f"\nThe choice of user is 'Paper'")
    elif choice == '3':
        print(f"\nThe choice of user is 'Scissors'")
    else:
        break

# getting reply from computer using random.randint module
    bot = random.randint(1,3)    
    if bot == 1:
        print(f"The choice of bot is 'Rock'\n")
    elif bot == 2:
        print(f"The choice of bot is 'Paper'\n")
    elif bot == 3:
        print(f"The choice of bot is 'Scissors'\n")
    
# checking if scores are 0 for draw, 1 for win and -1 for lose    
    score = check(bot, int(choice))
    if score == 0:
        print("It's a draw!")
    elif score == 1:
        print("Congrats, you beat the bot, you won!")
    elif score == -1:
        print("Unfortunately, The bot beaten you, you lost!")
