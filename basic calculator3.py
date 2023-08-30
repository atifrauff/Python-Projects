# Creating a fully functional calculator but with basic functions
print("Welcome to Our Latest Calculator v3.0!")
# Taking any number input from user
num1 = float(input("\nEnter Your First Number:\t"))
num2 = float(input("Enter Your Second Number:\t"))
# Taking sign of the operation
sign = input("Enter the Operation That You Want to Execute: ")
# Using 'if' and 'elif' statements to execute the sign in numbers
if sign == "+":
    print(f"The Addition of {num1} and {num2} is = ", f"' {num1+num2} '")
elif sign == "-":
    print(f"The Subtraction of {num1} and {num2} is = ", f"' {num1-num2} '")
elif sign == "*":
    print(f"The Multiplication of {num1} and {num2} is = ", f"' {num1*num2} '")
elif sign == "/":
    print(f"The Division of {num1} by {num2} is = ", f"' {num1/num2} '")
elif sign == "%":
    print(f"The Modulus of {num1} and {num2} is = ", f"' {num1%num2} '")
# if user want any other calculation rather than basic functions, this error will show up
else:
    print("Sorry, We Can't Execute this Command till this Version.")
# Final statement
print("\nStay Tuned With Us for Future Updates!")
