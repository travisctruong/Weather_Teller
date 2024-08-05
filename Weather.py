import requests
import datetime as dt


def determine_weather(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = 'b0e29d7179ee4a15b8319cdef3e8c234'

    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    data = requests.get(url).json()

    print("City:", city.capitalize())
    print("Weather Condition:", data['weather'][0]['description'].capitalize())
    print("Current Temperature:", str(round(kelvin_to_celsius(data['main']['temp']))) + "C")
    print("Feels like:", str(round(kelvin_to_celsius(data['main']['feels_like']))) + "C")
    print("H:" + str(round(kelvin_to_celsius(data['main']['temp_max']))) + "C", "L:" + str(round(kelvin_to_celsius(data['main']['temp_min']))) + "C")
    print("Humidity: " + str(data['main']['humidity']) + "%")
    print("Wind: " + str(data['wind']['speed']) + " m/s")
    print("Sunrise:", dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone']), "local time")
    print("Sunset:", dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone']), "local time")
    print()

    # image_url = "https://openweathermap.org/img/w/" + data['weather']['icon'] + ".png"

    # print(data)


def kelvin_to_celsius(temp):
    return temp - 273.15
