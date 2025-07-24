"""Create a file called mood_logger_v2.py that:
Asks the user how they feel
Saves it into a JSON file called mood_log.json
Appends new moods each time (not overwrite!)"""
from datetime import datetime
import json,os
mood=input("How are you feeling today:")
timestamp=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
entry={"mood":mood,"Timestamp":timestamp}
if not os.path.exists("mood_log.json"):
    mood_list = []
else:
    with open("mood_log.json", 'r') as f:
        try:
            mood_list = json.load(f)
        except json.JSONDecodeError:
            mood_list = []
mood_list.append(entry)
with open("mood_log.json", 'w') as f:
    json.dump(mood_list, f, indent=2)
print("Mood saved")
