import requests
import geocoder
import datetime
import json
from WeatherData import WeatherData

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt", "r").read()


def generate_url(city: str):
    return BASE_URL + "appid=" + API_KEY + "&q=" + city + "&lang=ru" + "&units=metric"


def get_user_city():
    return geocoder.ip("me").city


def save_weather_data(weather_data):
    with open('wd.json', 'a') as file:
        json.dump(weather_data.data, file, indent=0)


def parse_weather_data(resp):
    try:
        timezone = datetime.timezone(datetime.timedelta(seconds=float(resp["timezone"])))
        time = datetime.datetime.fromtimestamp(float(resp["dt"]), timezone)
    except KeyError:
        time = resp["time"]
        # для чтения из json
    name = resp["name"]
    description = resp["weather"][0]["description"]
    temp_celsius = resp["main"]["temp"]
    feels_like_celsius = resp["main"]["feels_like"]
    speed = resp["wind"]["speed"]
    weatherdata = WeatherData(time, name, description, temp_celsius, feels_like_celsius, speed)
    return weatherdata


def weather_for_selected_city():
    city = input("Введите город:\n").replace(" ", "")
    url = generate_url(city)
    response = requests.get(url).json()
    if response["cod"] == 200:
        weatherdata = parse_weather_data(response)
        save_weather_data(weatherdata)
        print(weatherdata, "\n")
    else:
        print(f"Ошибка {response['cod']}: {response['message']}")


def weather_for_user_city():
    city = get_user_city()
    url = generate_url(city)
    response = requests.get(url).json()
    weatherdata = parse_weather_data(response)
    save_weather_data(weatherdata)
    print(weatherdata, "\n")