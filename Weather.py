import requests
import datetime as dt

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "b0e29d7179ee4a15b8319cdef3e8c234"
CITY = "Toronto"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
data = requests.get(url).json()



print(data)
