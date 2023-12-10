class WeatherData:
    data = {"time": "", "city_name": "", "description": "", "temp_celsius": "", "feels_like_celsius": "",
            "speed": ""}

    def __init__(self, time, city_name, description, temp_celsius, feels_like_celsius, speed):
        self.data["time"] = str(time)
        self.data["city_name"] = str(city_name)
        self.data["description"] = str(description)
        self.data["temp_celsius"] = str(round(float(temp_celsius),2))
        self.data["feels_like_celsius"] = str(round(float(feels_like_celsius),2))
        self.data["speed"] = str(speed)

    def __str__(self):
        return (f"Текущее время: {self.data['time']}\n"
                f"Название города: {self.data['city_name']}\n"
                f"Погодные условия: {self.data['description']}\n"
                f"Текущая температура: {self.data['temp_celsius']} градусов по Цельсию\n"
                f"Ощущается как: {self.data['feels_like_celsius']} градусов по Цельсию\n"
                f"Скорость ветра: {self.data['speed']} м/с")