import json
data=[{"mood":"happy","timestamp":"2025-07-22 10:10"}]
with open ("data.json",'w') as f:
    json.dump(data,f)
with open ("data.json","r") as f:
    content= json.load(f)
    print(content)