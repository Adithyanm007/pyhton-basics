"""Combine reading and writing:
Ask if the user wants to view or add a note
If viewing: read and show file content (if it exists)
If adding: ask for a note and save it (append mode)"""
from datetime import datetime
import os
in1=int(input("Do u want to view (type 1) or add a note (type 0)"))
if in1==1:
    try:
        with open("notes.txt",'r') as f:
            contents=f.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")
else:
    if not os.path.exists("notes.txt"):
        try :
            with open("notes.txt",'w') as f:
                name=input("Enter your name:")
                note=input("Enter your note")
                timestamp=datetime.now().strftime("%d/%m/%y,%H:%M:%S")
                f.write("Note contents:\n")
                f.write(f"[{timestamp}] {name}: {note}\n")
        except FileNotFoundError:
            print("File not found.")
    else:
        try :
            with open("notes.txt",'a') as f:
                name=input("Enter your name:")
                note=input("Enter your note")
                timestamp=datetime.now().strftime("%d/%m/%y,%H:%M:%S")
                f.write(f"[{timestamp}]{name}: {note}\n")
        except FileNotFoundError:
            print("File not found.")
        
