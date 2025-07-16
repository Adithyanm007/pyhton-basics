import requests
url="https://api.adviceslip.com/advice"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print(f"Advice {data['slip']['advice']}")
else:
    print("Failed to retrieve advice")