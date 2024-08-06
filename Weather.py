import datetime as dt
import tkinter as tk


def kelvin_to_celsius_fahrenheit(temp, unit):
    """
    Converts Kelvin to Celsius or Fahrenheit

    Parameters:
        temp (float): degrees in Kelvin
        unit (string): unit to convert to

    Returns:
        Degrees in Celsius/Fahrenheit
    """
    if unit == "Celsius":
        return temp - 273.15
    else:
        return (temp - 273.15) * 1.8 + 32


def determine_weather(root, data, unit):
    """
    Processes weather data

    Parameters:
        root (tk): main application window
        data (str): current weather information of city
        unit (str): temperature unit to use

    Returns: None
    """
    # Initializes new window to display weather
    weather_window = tk.Toplevel(root, width=400, height=500, bg="#82CAFF")
    weather_window.title(data['name'] + " Weather")

    # Initializes city label
    city_label = tk.Label(weather_window, text=data['name'] + ", " + str(data['sys']['country']), bg="#82CAFF",
                          fg="white", font=("TkHeaderFont", 20))
    city_label.place(relx=0.5, rely=0.1955, anchor="center")

    # Initializes current temperature label
    current_temp_label = tk.Label(weather_window,
                                  text=str(round(kelvin_to_celsius_fahrenheit(data['main']['temp'], unit))) + "°",
                                  bg="#82CAFF", fg="white", font=("TkMenuFont", 48))
    current_temp_label.place(relx=0.5, rely=0.3, anchor="center")

    # Initializes weather condition label
    condition_label = tk.Label(weather_window, text=data['weather'][0]['description'].capitalize(), bg="#82CAFF",
                               fg="white", font=("TkHeaderFont", 20))
    condition_label.place(relx=0.5, rely=0.39, anchor="center")

    # Initializes temperature range label
    temp_range_label = tk.Label(weather_window,
                                text="H: " + str(round(kelvin_to_celsius_fahrenheit(data['main']['temp_max'], unit))) +
                                     "°  L: " + str(round(kelvin_to_celsius_fahrenheit(data['main']['temp_min'], unit)))
                                     + "°", bg="#82CAFF", fg="white", font=("TkHeaderFont", 20))
    temp_range_label.place(relx=0.5, rely=0.46, anchor="center")

    # Initializes feels-like temperature label
    feels_like_label = tk.Label(weather_window,
                                text="Feels like: " + str(round(kelvin_to_celsius_fahrenheit(data['main']['feels_like'],
                                                                                             unit))) + "°", bg="#82CAFF"
                                , fg="white", font=("TkHeaderFont", 16))
    feels_like_label.place(relx=0.5, rely=0.6, anchor="center")

    # Initializes humidity label
    humidity_label = tk.Label(weather_window, text="Humidity: " + str(data['main']['humidity']) + "%", bg="#82CAFF",
                              fg="white", font=("TkHeaderFont", 16))
    humidity_label.place(relx=0.5, rely=0.65, anchor="center")

    # Initializes wind speed label
    wind_label = tk.Label(weather_window, text="Wind: " + str(data['wind']['speed']) + " m/s", bg="#82CAFF", fg="white",
                          font=("TkHeaderFont", 16))
    wind_label.place(relx=0.5, rely=0.7, anchor="center")

    # Initializes date label
    sunrise_datetime = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    date_only = sunrise_datetime.date()
    date_label = tk.Label(weather_window, text=str(date_only), bg="#82CAFF", fg="white", font=("TkHeaderFont", 20))
    date_label.place(relx=0.5, rely=0.075, anchor="center")

    # Initializes sunrise label
    sunrise_time = sunrise_datetime.time()
    sunrise_label = tk.Label(weather_window, text="Sunrise: " + str(sunrise_time) +
                                                  " local time", bg="#82CAFF", fg="white", font=("TkHeaderFont", 16))
    sunrise_label.place(relx=0.5, rely=0.8, anchor="center")

    # Initializes sunset label
    sunset_datetime = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    sunset_time = sunset_datetime.time()
    sunset_label = tk.Label(weather_window, text="Sunset: " + str(sunset_time) +
                                                 " local time", bg="#82CAFF", fg="white", font=("TkHeaderFont", 16))
    sunset_label.place(relx=0.5, rely=0.85, anchor="center")
