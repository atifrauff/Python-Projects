total_price  = []
total_items  = []
total_num    = []
total_amount = []


def store():

    while True:
            item = input("\nInput the Item Name or 'q' to quit :  ")

            if item.lower() == "q":
                break
            total_items.append(item.capitalize())


            try:
                amount = int(input("Input the price of item :             "))
            except:
                print("\nYou've Entered wrong price. Please Enter correctly.")
                amount = int(input("Input the price of item :             "))

            total_price.append(amount)


            try:
                item_num = int(input("Input the Total Number/Kg of Item :   "))
            except:
                print("\nYou've Entered wrong amount or item number. Please Enter correctly.")
                item_num = int(input("Input the Total Number/Kg of Item :   "))
                 
            total_num.append(item_num)


            new_amount = amount * item_num
            total_amount.append(new_amount)


store()

print("\n#\tItem Name\tPrice\tAmount\t:\tTotal Price\n")

for i in range(len(total_amount)):
    print(f"""{i+1}-\t{total_items[i]}\t\t{total_price[i]}\t{total_num[i]}\t:\t{total_amount[i]}\- Rs.""")

print(f"\n                                                {sum(total_amount)}\- Rs.")
print("\nThanks for using our program!")
