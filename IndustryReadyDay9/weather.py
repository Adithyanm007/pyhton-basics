import requests
city=input("Enter the city name:")
api_key="a4da75901b03fab2885b2f0a3358fd1d"
url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print(f"City: {data['name']}")
    print(f"Temperature {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind speed: {data['wind']['speed']} m/s")
else:
    print("City not found")
    
