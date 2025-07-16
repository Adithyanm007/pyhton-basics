#Calculate the sum of all numbers in a list
num=[]
in1=input("Enter the numbers")
num.append((in1))
# Split the input string into individual numbers and convert them to integers
num = [int(x) for x in in1.split()]
total = 0
for n in num:
    total+=n
print("The sum of all numbers in the list is:", total)
