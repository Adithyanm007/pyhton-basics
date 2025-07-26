import requests
num=int(input("Enter a number: "))
url=f"http://numbersapi.com/{num}?json"
res=requests.get(url)
if res.status_code==200:
    data=res.json()
    print(f"number fact: {data['text']}")
else:
    print("Number fact not found, please try again later.")