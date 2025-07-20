try:
    in1=int(input("Enter a number:"))
    print("You entered:", in1)
except ValueError:
    print("Invalid input! Please enter a number.")