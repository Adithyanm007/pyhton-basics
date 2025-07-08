num=int(input("Enter a number to be checked"))
for i in range(2,num):
    if num%i==0:
        print(f"{num} is not a prime no. for {i}")
        break
    if (i==num-1):
        print("It is a prime number")
