import requests
url="https://catfact.ninja/fact"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print(f"Cat facts: {data['fact']}")
else:
    print("Cat fact not found, please try again later.")