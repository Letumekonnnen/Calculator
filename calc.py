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