try:
    with open ("mood_log.txt",'r') as f:
        entries = f.readlines()
        for entry in entries:
            print(entry.strip())
except FileNotFoundError :
    print("File not found.")            