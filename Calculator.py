# Functions

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y != 0:
        return "Error"
    else:
        return x/y
    
def square(x,y):
    return x**y

def square_root(x,y):


# user input

operation = input("Operations (+, -, *, /, ^, square root) : ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))

# Perform operation

if operation == "off":
    exit()
elif operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
elif operation == "^":
    result = square(num1, num2)
elif operation == "√":
    result = square_root(num,1, num2)
else:
    result = "Invalid input"

print(f"Result: {result}")
