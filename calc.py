import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Invalid input for square root."

def calculator():
    print("Welcome to the Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    
    choice = input("Enter the number corresponding to the operation you want to perform: ")
    
    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid input. Please try again.")
        return
    
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    elif choice == '6':
        num1 = float(input("Enter the number: "))
    
    if choice == '1':
        result = add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result:", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Result:", result)
    elif choice == '5':
        result = power(num1, num2)
        print("Result:", result)
    elif choice == '6':
        result = square_root(num1)
        print("Result:", result)

calculator()