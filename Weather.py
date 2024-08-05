import datetime as dt
import tkinter as tk


def kelvin_to_celsius(temp):
    return temp - 273.15


def determine_weather(root, data, city):
    weather_window = tk.Toplevel(root, width=500, height=600, bg="#82CAFF")
    weather_window.title(city.capitalize() + " Weather")

    city_label = tk.Label(weather_window, text=city.capitalize() + ", " + str(data['sys']['country']), bg="#82CAFF",
                          fg="white", font=("TkHeaderFont", 20))
    city_label.place(relx=0.5, rely=0.2, anchor="center")

    current_temp_label = tk.Label(weather_window, text=str(round(kelvin_to_celsius(data['main']['temp']))) + "C",
                                  bg="#82CAFF", fg="white", font=("TkMenuFont", 55))
    current_temp_label.place(relx=0.5, rely=0.3, anchor="center")

    condition_label = tk.Label(weather_window, text=data['weather'][0]['description'].capitalize(), bg="#82CAFF",
                               fg="white", font=("TkHeaderFont", 20))
    condition_label.place(relx=0.5, rely=0.39, anchor="center")

    temp_range_label = tk.Label(weather_window, text="H: " + str(round(kelvin_to_celsius(data['main']['temp_max']))) +
                                                     "C" + "  L: " +
                                                     str(round(kelvin_to_celsius(data['main']['temp_min']))) + "C",
                                bg="#82CAFF", fg="white", font=("TkHeaderFont", 20))
    temp_range_label.place(relx=0.5, rely=0.45, anchor="center")

    feels_like_label = tk.Label(weather_window, text="Feels like: " +
                                                     str(round(kelvin_to_celsius(data['main']['feels_like']))) + "C",
                                bg="#82CAFF", fg="white", font=("TkHeaderFont", 16))
    feels_like_label.place(relx=0.5, rely=0.6, anchor="center")

    humidity_label = tk.Label(weather_window, text="Humidity: " + str(data['main']['humidity']) + "%", bg="#82CAFF",
                              fg="white", font=("TkHeaderFont", 16))
    humidity_label.place(relx=0.5, rely=0.65, anchor="center")

    wind_label = tk.Label(weather_window, text="Wind: " + str(data['wind']['speed']) + " m/s", bg="#82CAFF", fg="white",
                          font=("TkHeaderFont", 16))
    wind_label.place(relx=0.5, rely=0.7, anchor="center")

    sunrise_datetime = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    date_only = sunrise_datetime.date()
    date_label = tk.Label(weather_window, text=str(date_only), bg="#82CAFF", fg="white", font=("TkHeaderFont", 20))
    date_label.place(relx=0.5, rely=0.075, anchor="center")

    sunrise_time = sunrise_datetime.time()
    sunrise_label = tk.Label(weather_window, text="Sunrise: " + str(sunrise_time) +
                                                  " local time", bg="#82CAFF", fg="white", font=("TkHeaderFont", 16))
    sunrise_label.place(relx=0.5, rely=0.8, anchor="center")

    sunset_datetime = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    sunset_time = sunset_datetime.time()
    sunset_label = tk.Label(weather_window, text="Sunset: " + str(sunset_time) +
                                                 " local time", bg="#82CAFF", fg="white", font=("TkHeaderFont", 16))
    sunset_label.place(relx=0.5, rely=0.85, anchor="center")
    print(data)