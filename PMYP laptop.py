# creating complaint chart for PMYP laptop scheme
user=input("""Do you have any mistake in your data? 
Answer Yes or No: """)
match user:
    case _ if user.capitalize().strip(" ") == "Yes":
        print("\nClick 'Search Focal Person' from the Menu & find your University's Focal Person.")
        print("\nContact your 'University's Super Focal Person' with proper evidence regarding your data correction.")
        print("\nTake confirmation from 'Focal Person' regarding your data correction.")
        print("\nVerify your record by clicking 'Application Status' from Menu.")
        user2=input("""Have you followed all of these steps?
Answer 'Yes' or 'No': """)
        if user2.capitalize().strip(" ")=="Yes":
            print("That's great, you've applied succesfully!")
        if user2.capitalize().strip(" ")=="No":
            print("Sorry, you should repeat the process to get verified.")
    case _ if user.capatalize().strip(" ")=="No":
        print("That's great, you've applied succesfully!")
