def pkr_to_currency():

    with open("Python Projects/currencyData August 2023.txt") as f:
        lines = f.readlines()

    currency_dict = {}
    for line in lines:
        parsed = line.split("\t")
        currency_dict[parsed[0]] = parsed[1]

    while True:
        try:
            amount = input("\nEnter the amount of Rupees you want to convert :      ")
        
            if amount.lower() == "quit":
                break

            [print(keys) for keys in currency_dict.keys()]

            choice = input("\nEnter the currency name by copying from above :\n")
            
            if choice.lower() == "quit":
                break

            print(f"\nAs of August 2023, {amount}/- Rs. to {choice} is :    {float(amount) * float(currency_dict[choice])}")
            break

        except:
            print("You've Encountered an Error. Please Give Correct Required Info.\n")


def currency_to_pkr():

    with open("Python Projects/currencyData August 2023.txt") as f:
        lines = f.readlines()

    currency_dict = {}
    for line in lines:
        parsed = line.split("\t")
        currency_dict[parsed[0]] = parsed[1]

    while True:
        try:
            amount = input("\nEnter the amount of money you want to convert in Pkr :      ")
            
            if amount.lower() == "quit":
                break

            [print(keys) for keys in currency_dict.keys()]
            choice = input("\nEnter the currency name by copying from above :\n")
            
            if choice.lower() == "quit":
                break

            print(f"\nAs of August 2023, {amount}/- {choice} to Pakistani Rupees is :    {float(amount) * float(currency_dict[choice])}/- Rs.")
            break

        except:
            print("You've Encountered an Error. Please Give Correct Required Info.\n")


def currency_converter():
    print("Welcome to Our Currency Converter Program v1.0\n")
    print("We are so excited to present you our program.")
    print("If you want to close the program anytime, input 'quit'")
    print("Press ENTER to continue...")
    user = input("")
    
    if user.lower() == "quit":
        exit()

    while True:
        user = input("""Enter '1' if you want to convert pkr to any currency
Enter '2' if you want to convert any currency to pkr
""")

        if user.lower() == "quit":
            break

        if user == "1":
            pkr_to_currency()
            break

        elif user == "2":
            currency_to_pkr()
            break

        else:
            print("\nYou've entered the wrong input. Please input correctly.\n")


if __name__ == "__main__":
    currency_converter()
