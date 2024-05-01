import json

# install and import request. Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!
import requests
import json

# take the city input from user
city = input("Pl enter the name of the city: ")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# open the api key and store in a variable
API_KEY = open("api_key.text", "r").read()
url = BASE_URL + "&q=" + city + "&units=imperial" + "&appid=" + API_KEY
# now make the rquest to that website
weather_data = requests.get(url).json()

if weather_data['cod'] == str(404):
    print("city not found")

else:
    # weather_data1 = json.loads(weather_data)
    print(weather_data)

    city_temp = weather_data['main']['temp']

    def farenheit_to_celsius_converter (farenheit):
            temp = farenheit
            celsius = (temp - 32) * 5/9
            return celsius
    city_temp_celsius= farenheit_to_celsius_converter(city_temp)

    print(f"The temperature in {city} city is: {city_temp} degree farenheit or {city_temp_celsius} degree celsius")

    city_weather = weather_data['weather'][0]['main']
    print(f"Weather in {city} city is: {city_weather}")

    city_min_temp = weather_data['main']['temp_min']
    city_min_temp_celsius = farenheit_to_celsius_converter(city_min_temp)

    print(f"The min temperature in {city} city is: {city_min_temp} degree farenheit or {city_min_temp_celsius} degree celsius")
    # print(weather_temp)
