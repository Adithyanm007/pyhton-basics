with open('file.txt','w') as file:
    file.write("Python lets you open, read, write, and append to files")
with open('file.txt','r') as file:
    contents=file.read()
    print(contents)