# we're creating Kon Banega Crorepati KBC version 2

# take name as input with capital initials
name = input("Enter Your Name   :      ")
named = name.title().strip(" ")

# function that will give resposnes on the basis of age and gender
def age_gender():
    age = input("Enter your Age    :      ")
    if int(age) >= 18:
        gender = input("Male or Female    :      ")
        if gender.capitalize().strip(" ") == "Male":
            print(f"\n------>>>     Welcome to KBC, Mr. {named}     <<<------\n")
        elif gender.capitalize().strip(" ") == "Female":
            print(f"\n------>>>     Welcome to KBC, Miss. {named}     <<<------\n")
        else:
            raise TypeError("Sorry, invalid response!")
    else:
        raise ValueError("Sorry, you're not eligible!")

# calling the function
age_gender()

# printing basic rules and guidelines
print("""Here are some rules that you must keep in mind while playing the game:
1- You have to reply in given indexes of 1/2/3/4
2- Only on a certain level, you'll awarded with money
3- You'll be asked to quit after every question, if you want to quit, enter 'quit'.
Your money will be transferred to you, and the game would be ended.
Otherwise, you'll earn only levels' money

            Levels of the Game
--> 'Ground Level'  =   Rs. 10,000/- after First Question
--> 'Level One'     =   Rs. 30,000/- after Three Questions
--> 'Level Two'     =   Rs. 50,000/- after Five Questions 
--> 'Final Level'   =   Jackpot of One Million Rs.
      
""")

print("Read the guidelines carefully!")
input("Press Enter, when you're ready to start the game...     ")
print("""                
                Let's Start the Game NOW !!!
                        _BEST OF LUCK_
""")

# list of questions that would be asked with options and correct answer
questions = [
[
    "Which companion of the Prophet Muhammad Saww is called 'Raz-daar e Rasool'?",
    "Abu Bakr   ", "Abdullah Ibne Masood",
    "Mola Ali   ", "Huzaifa bin Yaman", 4
],
[
    "Which country is not included in BRICS movement?",
    "India    ", "Saudi Arabia", 
    "Russia   ", "China", 2
],
[
    "Who invented the first Hydrogen-Bomb?",
    "A. Einstein", "R. Oppenheimer", 
    "E. Teller  ", "N. Bohr", 3
],
[
    "Who played the Oscar winning iconic role of 'Joker'?",
    "Tom Hiddleston   ", "Tom Holland", 
    "Jacquine Pheonix ", "Heath Ledger", 4
],
[
    "Which ruler's era is considered as 'Golden Era' of Pakistan's history?",
    "Gen. Ayub Khan   ", "Zulfiqar Ali Bhutto", 
    "Gen. Zia-ul Haqq ", "Nawaz Sharif", 1
],
[
    "Which Army Chief General launched operations 'Zarb-e-Azb' and 'Radul Fasaad' in Pakistan?",
    "Gen. Pervaiz Musharraf ", "Gen. Asim Munir", 
    "Gen. Raheel Shareef    ", "Gen. Zia-ul Haqq", 3
],
[
    "Which companion of Prophet Muhammad Saww was killed for not cursing Mola Ali?",
    "Abdullah Ibne Masood ", "Hujr Ibne Adi" ,
    "Ammar Ibne Yasir     ", "Muhammad Bin Abi-Bakr", 2
],
[
    "Who gave the idea of Wormholes?",
    "A. Einstein    ", "Sir George Fredrick", 
    "Micheal Farady ", "Schrodinger", 1
],
[
    "Who is considered as the Father of Modern Computer Science?",
    "Alan Turing     ", "Charles Babbage", 
    "John von Neumann", "Vint Cerf", 1
],
[
    "Who accepted Islam after Hazrat Khadija on the hands of Holy Prophet Saww?",
    "Abu Bakr   ", "Hamza bin Abi Talib", 
    "Mola Ali   ", "Zaid Ibne Harisa", 3
],
            ]

# now we'll add three levels in the list
levels = [
    10000,
    30000,
    50000,
    100000
]

# initializing money value to zero for increasing if user reach any level
money = 0
# we'll use 'for loop' for questioning and answering
for index, i in enumerate(range(0, len(questions)), start=1):
    question = questions[i]
    print(f"\n\n{index}- {question[0]}")
    print(f" I-  {question[1]}                II- {question[2]}")
    print(f"III- {question[3]}                IV- {question[4]}")
    
    # using input functsion we'll take reply from user and storing it in answer variable
    answer = int(input("\n----->>>>   "))
    if answer == question[-1]:
        print("\nCorrect Answer!")
        if i == 0:
            print("Congrats! You've reached the Ground level.")
            input("You don't have to quit right now, Keep Going by pressing ENTER...   ")
            money == 10000
        elif i == 1:
            print("You've won 20,000/- Rs. so far")
            quit = input("If you want to quit right now, type 'quit', or Keep Going by pressing ENTER...   ")
            if quit.lower() == "quit":
                print("\nThe game has ended on your demand!")
                print("Your take home money is Rs. 20,000/-")
                print("Thanks for playing with Us!")
                break
        elif i == 2:
            print("Congrats! You've reached the level ONE.")
            input("You don't have to quit right now, Keep Going by pressing ENTER...   ")
            money == 30000
        elif i == 3:
            print("You've won 40,000/- Rs. so far")
            quit = input("If you want to quit right now, type 'quit', or Keep Going by pressing ENTER...   ")
            if quit.lower() == "quit":
                print("\nThe game has ended on your demand!")
                print("Your take home money is Rs. 40,000/-")
                print("Thanks for playing with Us!")
                break
        elif i == 4:
            print("Congrats! You've reached the level TWO.")
            input("You don't have to quit right now, type 'quit', or Keep Going by pressing ENTER...   ")
            money == 50000
        elif i == 5:
            print("You've won 60,000/- Rs. so far")
            quit = input("If you want to quit right now, type 'quit', or Keep Going by pressing ENTER...   ")
            if quit.lower() == "quit":
                print("\nThe game has ended on your demand!")
                print("Your take home money is Rs. 60,000/-")
                print("Thanks for playing with Us!")
                break
        elif i == 6:
            print("You've won 70,000/- Rs. so far")
            quit = input("If you want to quit right now, type 'quit', or Keep Going by pressing ENTER...   ")
            if quit.lower() == "quit":
                print("\nThe game has ended on your demand!")
                print("Your take home money is Rs. 70,000/-")
                print("Thanks for playing with Us!")
                break
        elif i == 7:
            print("You've won 80,000/- Rs. so far")
            quit = input("If you want to quit right now, type 'quit', or Keep Going by pressing ENTER...   ")
            if quit.lower() == "quit":
                print("\nThe game has ended on your demand!")
                print("Your take home money is Rs. 80,000/-")
                print("Thanks for playing with Us!")
                break
        elif i == 8:
            print("You've won 90,000/- Rs. so far")
            quit = input("If you want to quit right now, type 'quit', or Keep Going by pressing ENTER...   ")
            if quit.lower() == "quit":
                print("\nThe game has ended on your demand!")
                print("Your take home money is Rs. 90,000/-")
                print("Thanks for playing with Us!")
                break
        elif i == 9:
            print("\n\nAmazing! You've won JACKPOT!!!")
            # final statements as the game ended by winning
            print("It was an Honor for Us for Playing With YOU")
            print("Your Take Home Money is Rs. One Million!!!")
            print("We'll Contact You As Soon As Our Next Game is Launched!")
            break

    # if user typed any other number apart from 1-4, raise error
    elif answer > 4 or answer == 0:
        raise ValueError("Sorry, invalid input!")
    
    # if any time the answer is wrong, stop the program and tell their take away money
    else:
        print("\nWrong Answer!")
        print("We apologize, but you can't continue anymore")
        if index == 1:
            print("\nIt's a shame for Us for having you as player!")
            break
        # final statements as the game ended 
        print("\nWe're pleased for playing with you!")
        print(f"Your take home money is Rs. {money}/-")
        print("Thanks for playing with Us!")
        break

