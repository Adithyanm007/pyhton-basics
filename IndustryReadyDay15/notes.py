"""Accepts your name and a note from the user.
Saves it to a file called notes.txt.
Reads the content from notes.txt and displays it."""
import os
inp=input("Enter your name:")
note=input("Enter your note:")
if  not os.path.exists('notes.txt'):
    with open('notes.txt','w') as file:
        file.write(f"Your notes: \n {inp}: {note} ")
else:
    with open('notes.txt','a') as file:
        file.write(f"\n{inp}: {note} ")
with open('notes.txt','r') as file:
    contents=file.read()
    print(contents)    

