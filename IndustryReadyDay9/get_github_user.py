import requests
username=input("Enter GitHub username: ")
url=f"https://api.github.com/users/{username}"
response=requests.get(url)
if response.status_code==200:
    data = response.json()
    print(f"Name: {data['name']}")
    print(f"Repo: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
else:
    print("User not found")