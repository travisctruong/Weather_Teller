import requests


def obtain_data(city):
    """
    Uses API key and URL to generate weather information

    Parameters:
        city (str): user specified city to check weather of

    Returns:
        data (str): current weather information of city
        None: if user enters improper city name
    """
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = 'b0e29d7179ee4a15b8319cdef3e8c234'

    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    # image_url = "https://openweathermap.org/img/w/" + data['weather']['icon'] + ".png"
    data = requests.get(url).json()

    if data['cod'] == 200:         # Checks if a response from host is received
        return data
    else:
        return None
