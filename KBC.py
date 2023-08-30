# first we'll assign questions and answers in the list of list
questions = [
[
    "What is the capital of Pakistan?", "Lahore", "Islamabad", "Quetta", "None", 2
    ],
[
    "What is the currency of Russia?", "PKR", "INR", "RUB", "USD", 3
    ],
[
    "What is the highest mountain peak in World?", "Mount Everest", "K-2", "Margrilla Hills", "Northern Hills", 1
    ]
]

# now we'll define the levels of amount the person is winning
levels = [
10000,
30000,
50000
]
money = 0
# using for loop for displaying qestions and options to display
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    
# we'll also take reply in for loop for all of the questions and check right here    
    reply = int(input("""\nEnter your answer (1-4):
>>>>>>>>  """))
    if reply < 1 or reply > 4:
        raise ValueError("Wrong index, please choose between 1-4!")
    elif reply == question[-1]:
        print(f"Correct Answer! You have won Rs. {levels[i]}")
        if i == 0:
            money = 10000
        elif i == 1:
            money = 30000
        elif i == 2:
            money = 50000
# program will break if the reply is wrong
    else:
        print("Wrong Answer!")
        print("The game is ending...")
        break
print("\nThe game has ended!")
print(f"Your take home money is Rs. {money}/-")
print("Thanks for playing with Us!")

# # Check if questions are Correct
# def check(questions,answers):
#     if answer.title()==answers[questions].title():
#         return True
#     else:
#         return False
# # Functions to play the game


# name = input("Assalam o Alaikum Sir, what's your name? ")
# print("Congrats",name.title().strip(' ')+", you've been selected for KBC.")
# answer = input("Do you want to play this game with Us? Yes or No: ")
# if answer.capitalize().strip(' ')=="No":
#     print("No problem Sir, you're free to go.")
# elif answer.capitalize().strip(' ')=="Yes":
#     print("""\nThat's great, so, we should start with the rules first: 
# 1- You have to give response in 'a', 'b', 'c', 'd'.
# 2- The answer should not be other than above options, otherwise, you'll be disqualified.
# 3- You have to play the game till the last Question. There would be total 3 Questions.
# 4- The amount of money you would win, based on your correct answers, will be displayed to you in the end.
# 5- Overall, you can win 50,000\- Rs. if all of the questions are correct.""")
#     start = input("Let's start the game, are you ready? Yes or No: ") 
#     if start.capitalize().strip(" ")=="No":
#         print("No prob. Sir. When you're ready, re-run the program to start again.")
#     elif start.capitalize().strip(" "):
#         pass
#     else:
#         print("Sorry Sir, this is invalid response. Kindly re-run the program to give correct response!")    
# else:
#     print("Sorry Sir, this is invalid response. Kindly re-run the program to give correct response!")
