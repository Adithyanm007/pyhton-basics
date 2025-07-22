try:
    with open("file2.txt") as file:
        read=file.read()
        print(read)
except FileNotFoundError as err:
    print(err)
