with open('file.txt','r') as f:
    for _ in f.readline():
        content=f.readline()
        print(content)