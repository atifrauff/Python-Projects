''' We're creating a number checker program
which will identify whether given number is
decimal or integer. If integer then a positive
or negative even/odd integer or just a zero.
'''
print("Welcome to Our Number Checker v2.0!")
# Taking input from user
num = input("\nEnter Your Number: ")
# Using 'if' for first checking whether it's decimal
if '.' in num:
    print("Your Number is Not an Integer, it's a Decimal Number.")
# Using 'elif' for checking if a number is zero
elif int(num) == 0:
    print("Your Number is 'Zero'")
# Using 'else' for checking if it's an integer
else:
# Casting string to integer because it's already confirmed that the number is not decimal
    num = int(num)
# Using 'if' we'll find whether the number is completely divisible by 2 by using modulus
    if num%2 == 0:
# Checking if number is greater than zero
        if num>0:
            print(f"'{num}' is Positive, Even Integer.")
# Checking if number is smaller than zero
        elif num<0:
            print(f"'{num}' is Negative, Even Integer.")
# If the remainder of number modulus 2 is 1, then it's odd
    elif num%2 == 1:
# Checking if number is greater than zero
        if num>0:
            print(f"'{num}' is Positive, Odd Integer.")
# Checking if number is smaller than zero        
        elif num<0:
            print(f"'{num}' is Negative, Odd Integer.")
# Final statement
print("\nThanks for Using Our Number Checker v2.0!")
