import datetime as dt
import time as t

import requests
import geocoder
from time import gmtime, strftime

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt", "r").read()


def generate_url(city: str):
    '''
    generates url to request weather for selected city
    '''
    return BASE_URL + "appid=" + API_KEY + "&q=" + city


def get_user_city():
    return geocoder.ip("me").city


def parse_weather_data(resp):
    time = (t.strftime("%Y-%m-%d ", t.gmtime()) + str(t.gmtime().tm_hour + resp["timezone"]//3600) +
            t.strftime(":%M:%S", t.gmtime()))
    name = resp["name"]
    description = resp["weather"][0]["description"]
    temp_celsius = kelvin_to_celsius(resp["main"]["temp"])
    feels_like_celsius = kelvin_to_celsius(resp["main"]["feels_like"])
    speed = resp["wind"]["speed"]
    weatherdata = WeatherData(time, name, description, temp_celsius, feels_like_celsius, speed)
    return weatherdata


def kelvin_to_celsius(temp):
    return temp - 273.15


class WeatherData:
    def __init__(self, time, city_name, description, temp_celsius, feels_like_celsius, speed):
        self.time = str(time)
        self.city_name = str(city_name)
        self.description = str(description)
        self.temp_celsius = str(temp_celsius)
        self.feels_like_celsius = str(feels_like_celsius)
        self.speed = str(speed)

    def __str__(self):
        return (f"Текущее время: {self.time}\n"
                f"Название города: {self.city_name}\n"
                f"Погодные условия: {self.description}\n"
                f"Текущая температура: {self.temp_celsius}\n"
                f"Ощущается как: {self.feels_like_celsius}\n"
                f"Скорость ветра: {self.speed}")


def enable_cycle():
    while True:
        city = input("Введите город:\n")
        if city == "хватит":
            break
        url = generate_url(city)
        response = requests.get(url).json()
        weatherdata = parse_weather_data(response)
        print(weatherdata, "\n")


if __name__ == "__main__":
    enable_cycle()
