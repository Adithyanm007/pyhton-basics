"""Create a calculator that:
Accepts two numbers and an operation (+, -, *, /)
Performs the operation
Handles exceptions like:
Division by zero
Invalid inputs"""
in1=input("Enter a expression")
try:
    result = eval(in1)
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Enter a number")
except SyntaxError:
    print("Invalid input! Please enter a valid expression.")
