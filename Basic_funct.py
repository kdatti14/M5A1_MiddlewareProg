# Define basic functions

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Error! Cannot divide by zero!"
    else:
        return x / y

# Function calls

print("Addition:", add(5, 3))  # Output: 8
print("Subtraction:", subtract(7, 2))  # Output: 5
print("Multiplication:", multiply(4, 6))  # Output: 24
print("Division:", divide(10, 2))  # Output: 5.0
print("Division by zero:", divide(8, 0))  # Output: Error! Cannot divide by zero!
