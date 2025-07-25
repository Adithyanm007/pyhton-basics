import requests
url="https://official-joke-api.appspot.com/random_joke"
response=requests.get(url)
if response.status_code==200:
    joke=response.json()
    print(f"{joke['setup']}\n")
    print(f"{joke['punchline']}")
else:
    print("Joke not found, please try again later.")