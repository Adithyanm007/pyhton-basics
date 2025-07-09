try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result=a/b
    print(f"The result of {a}/{b}={result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
