# Creating a basic calculator with two inputs
print('\nHey there! Do you want to calculate anything?')
print('''I can help you. Just give any two numbers whose calculations you want.
And I\'ll give the Addition, Subtraction, Multiplication and Division of those numbers.\n''')

a = int(input('Write your First Number:\t'))
b = int(input('Write your Second Number:\t'))
Addition = a+b
Subtraction = a-b
Multiplication = a*b
Division = a/b
print('\nYour Calculations are:')
print(f'Addition of {a} and {b} is:\t\t{a} + {b}  =', Addition)
print(f'Subtraction of {a} and {b} is:\t{a} - {b}  =', Subtraction)
print(f'Multiplication of {a} and {b} is:\t{a} x {b}  =', Multiplication)
print(f'Division of {a} by {b} is:\t\t{a} / {b}  =', Division)
print('\nThanks for Using Our Calculator!')