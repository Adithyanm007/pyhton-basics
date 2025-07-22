from datetime import datetime
mood=input("How are u feeling today:")
timestamp=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
with open("mood_log.txt",'a') as f:
    f.write(f"[{timestamp}] {mood}")
print("mood saved")