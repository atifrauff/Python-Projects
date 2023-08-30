print("Welcome to Our Number Identifier v1.0!")
print("Till Now, We can Only Tell if a number is Even or Odd.")
print("Stay Tuned With Us for More Functions!")
num = int(input("\nEnter Your Number: "))
if num%2 == 0:
    print(f"Your Number '{num}' is an Even Number")
elif num == 0:
    print(f"Your Number '{num}' is Zero")
else:
    print(f"Your Number '{num}' is an Odd Number")
print("\nThanks for Using Our First Even, Odd Number Checker!")
