from functions import *
from WeatherData import WeatherData
from consts import *


def read_history():
    try:
        n = int(input("Сколько запросов?\n"))
        weather_datas = read_weather_data(n)
        weather_datas.reverse()
        for wd in weather_datas:
            wdprint = WeatherData(*wd.values())
            print(f"{wdprint}\n")
            del wdprint
    except ValueError:
        print('Число запросов выражается целым положительным числом')


def read_weather_data(n: int):
    if (type(n) != int) or (n < 1):
        raise ValueError
    else:
        data_array = []
        with open('wd.json', 'r') as file:
            remainder = file.read().replace("\n", "")
            while len(remainder) > 2:
                data_array.append(remainder.partition("}")[0] + "}")
                remainder = remainder.partition("}")[2]
        weather_data_array = []
        i = 1
        data_array.reverse()
        for d in data_array:
            if i > n:
                break
            js = json.loads(d)
            weather_data_array.append(js)
            i = i + 1
        return weather_data_array


def clear_history():
    with open("wd.json", "w") as file:
        pass


options = {"1": weather_for_user_city,
           "2": weather_for_selected_city,
           "3": read_history,
           "4": clear_history,
           "5": ""}



def enable_cycle():
    while True:
        answer = input(answer_prompt).replace(" ", "")
        if answer in options.keys():
            if answer == "5":
                break
            else:
                options[answer]()
        else:
            print('Нет такой опции')


if __name__ == "__main__":
    enable_cycle()
