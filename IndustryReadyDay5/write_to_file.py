txt=input("Enter a txt to enter into a file:")
with open("sample.txt","w") as file:
    file.write(txt)
    print("Data written to file successfully.")
file.close()