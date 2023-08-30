import sys

def addition(a,b):
    return a + b

def prime():
    n = 49
    if n == 2:
        return True
    elif n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(prime())

def main():

    if len(sys.argv) != 3:
        print("Usage: python day15.py num1 num2")
        return
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = addition(num1, num2)
        print("Result:  ",result)

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
