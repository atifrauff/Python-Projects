# let's create a voting machine
print("Welcome to Our Voting Machine v1.0")
# taking user input
x = input("Do You Want to Caste Vote? Answer Yes or No: ")
# making the input initials capitals and stripping if there's any spaces
v = x.capitalize().strip(" ")
# using match case statement to take different responses in different cases
match v:
# using case statement to check if the answer is yes
    case _ if v=="Yes":
# if yes, then ask about the age
        print("\nThat's great, we just want to confirm your age.")
        age = int(input("How old are you? "))
# if the age is equals or above 18, then print voting options        
        if age>=18:
            vote =int(input("""That's nice, you can caste vote.
\nWhom do you want to vote: 
1- Pakistan Muslim League Nawaz (PMLN)
2- Pakistan Tehreek-e-Insaf (PTI)
3- Pakistan Peoples's Party (PPP)
Enter the number of the party, please: """))
            if vote == 1:
                print("\nCongrats, your vote has been casted to PMLN!")
            elif vote == 2:
                print("\nCongrats, your vote has been casted to PTI!")
            elif vote == 3:
                print("\nCongrats, your vote has been casted to PPP!")
            else:
                print("""\nYou've entered the wrong command.
Kindly, again run the program to proceed again.""")
# if age is below 18, show this error
        else:
            print("\nSorry Sir, you can't caste vote as you're below 18.")
# second case if don't want to vote
    case _ if v=="No":
        print("\nNo problem, you can leave this program.")
 