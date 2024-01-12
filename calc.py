#calculator
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