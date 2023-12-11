import requests
import geocoder
import time as t
import json
from WeatherData import WeatherData

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt", "r").read()


def generate_url(city: str):
    return BASE_URL + "appid=" + API_KEY + "&q=" + city + "&lang=ru"


def get_user_city():
    return geocoder.ip("me").city


def kelvin_to_celsius(temp):
    return temp - 273.15


def save_weather_data(weather_data):
    with open('wd.json', 'a') as file:
        json.dump(weather_data.data, file, indent=0)


def parse_weather_data(resp):
    try:
        time = (t.strftime("%Y-%m-%d ", t.gmtime()) + str(t.gmtime().tm_hour + resp["timezone"]//3600) +
                t.strftime(":%M:%S", t.gmtime()))
    except KeyError:
        time = resp["time"]
        # для чтения из json
    name = resp["name"]
    description = resp["weather"][0]["description"]
    temp_celsius = kelvin_to_celsius(resp["main"]["temp"])
    feels_like_celsius = kelvin_to_celsius(resp["main"]["feels_like"])
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