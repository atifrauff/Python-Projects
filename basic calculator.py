# Creating a basic calculator

# a = int(input("What is your first number: "))
# b = int(input("What is your second number: "))
# add = a+b
# print("The addition of", a, "and", b, "is:\t\t", add)
# minus = a-b
# print("The subtraction of", a, "and", b, "is:\t\tw", minus)
# multiple = a*b
# print("The multiplication of", a, "and", b, "is:\t", multiple)
# division = a/b
# print("The division of", a, "by", b, "is:\t\t", division)
# modulus = a%b
# print("The modulus of", a, "and", b, "is:\t\t", modulus)
# floorD = a//b
# print("The floor division of", a, "and", b, "is:\t", floorD)


num1 = int(input("Write your first number: "))
num2 = int(input("Write your second number: "))
sign = input("What action do you want: ")[0]
result = num1 + sign + num2
print(result)
