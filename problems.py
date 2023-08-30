    ### Problem 1 - Radians to degrees ###

# defining a function to convert radians to degrees
def radDeg():

    # importing math module to use round off number later
    import math
    print("Welcome to our program. We'll help you convert radians into degrees.")
    number = int(input("Enter the number you want to convert in degrees :   "))

    # formula to convert radians into degrees
    degrees = number * (180 / 3.14)

    # printing the value of degrees upto three decimal points using round function
    print(f"\n'{number}' radians in degrees is '{round(degrees, 3)}'")

# calling the defined function
radDeg()


    ### Problem 2 - Radians to degrees ###

# initializing an empty list to store user input words later
listing = []

# definig a function to take user input and append in the above list
def addList():
    
    while True:
        # exception handling
        try:

            # taking user input and storing in variable user
            user = input("""\nEnter the numbers you want to put in the list or enter 'quit' to break:
        -------->>>>>     """)
            
            if user.lower() == "quit":
                break

            else:
                # appending user number into list
                listing.append(int(user))

                # printing the added number and the entire list so far
                print(f"\n'{int(user)}' has been added to the list.")
                print(listing)

        # not implemented error
        except NotImplementedError:
            print(f"\nYou've prompted an error:   {NotImplementedError}")

        # raising value error if user inputs random value
        except ValueError:
            print(f"You've prompted an error:   ", ValueError)
        
        # raising exception error if error is undefined
        except Exception:
            print(f"You've prompted an error:   ", Exception)

# defining a function to convert list of numbers in ascending order
def asc():

    # if list is empty, throw an error
    if len(listing) == 0:
        print("\nSorry, your list is empty!")

    # else sort using sorted function in ascending order and print sorted list
    else:
        sorted_list = sorted(listing)
        print(f"\nYour sorted list in Ascending Order is:\n{sorted_list}")

# defining a function to convert list of numbers in descending order
def desc():

    # if list is empty, throw an error
    if len(listing) == 0:
        print("\nSorry, your list is empty!")

    # else sort the list in descending order using sorted function and reverse=True method and then prints
    else:
        sorted_list = sorted(listing, reverse=True)
        print(f"\nYour sorted list in Descending Order is:\n{sorted_list}")


# creating user interface to interact with user
print("""\n```   Welcome to our Number Listing Program!   ```
It will take your numbers and add in the list. 
It can align it in ascending and descending order.""")

# using while True loop to run the program in loop as long as user wants to
while True:

    # exception handling if user don't work with guidlines
    try:

        # asking to ENTER everytime it starts around
        input("\nPress ENTER to Continue . . . ")

        # giving indexes of the functions that user can perform using this program
        print("\nEnter the INDEX of the function you want to execute:")
        print("""1 - Add Number in List
2 - Sort List in Ascending Order
3 - Sort List in Descending Order
0 - Break the Program

""")

        # taking input from user and storing in user variable
        user = int(input("------->>>>>      "))

        # if the input is 1, call addList() function
        if user == 1:
            addList()

        # if the input is 2, call asc() function
        elif user == 2:
            asc()
        
        # if the input is 3, call desc() function
        elif user == 3:
            desc()

        # if the input is 0, break the loop and eventually the whole program
        elif user == 0:
            break

        # else throw an error that user should use indexes between (0-3)
        else:
            print("\nInvalid input! You can only enter (0-3) for program to execute.")

    # throwing not implemented error
    except TypeError:
        print(f"\nYou've prompted an error:   {TypeError}")
    
    # throwing a value error
    except ValueError:
        print(f"\nYou've prompted an error:   {ValueError}")
    
    # if the error is undefined, throw exception error
    except Exception:
        print(f"\nYou've prompted an error:   {Exception}")
