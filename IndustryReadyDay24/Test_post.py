import requests
url='http://127.0.0.1:5000/data'
data={
    "name": "John Doe",
    "age": 30,
}
response=requests.post(url,json=data)
print(response.status_code)
print(response.json())