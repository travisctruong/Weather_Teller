import tkinter as tk
import Data
import Weather
from tkinter import *


def get_entry():
    """
    Obtains info from API and user input and sends data to be processed

    Parameters: None

    Returns: None
    """
    unit = selected.get()                     # Obtains temperature unit and city from user
    user_input = entry.get()
    entry.delete(0, tk.END)

    data = Data.obtain_data(user_input)         # Obtains data from API
    if data is None:
        error_window = tk.Toplevel(root, width=250, height=300, bg="white")
        error_window.title("Error")                                    # Opens error prompt if improper city is entered

        error_label = tk.Label(error_window, text="Invalid city name", bg="white", fg="red",
                               font=("TkHeaderFont", 20))
        error_label.place(relx=0.5, rely=0.5, anchor="center")
    else:
        Weather.determine_weather(root, data, unit)   # Sends data to be processed


# Initializes main window
root = tk.Tk()
root.title("Weather Teller")

main_frame = tk.Frame(root, width=500, height=600, bg="#3d6466")
main_frame.grid(row=0, column=0)
main_frame.pack_propagate(False)

# Initializes title label
title_label = tk.Label(main_frame, text="Weather Teller", bg="#3d6466", fg="white", font=("TkMenuFont", 24))
title_label.place(relx=0.5, rely=0.3, anchor="center")

# Initializes instruction label
instruction_label = tk.Label(main_frame, text="Please Enter a City", bg="#3d6466", fg="white",
                             font=("TkHeaderFont", 12))
instruction_label.place(relx=0.5, rely=0.375, anchor="center")

# Initializes dropdown list for different temperature units
units = ["Celsius", "Fahrenheit"]
selected = tk.StringVar()
selected.set(units[0])
units_dropdown = OptionMenu(main_frame, selected, *units)
units_dropdown.config(width=20)
units_dropdown.place(relx=0.5, rely=0.5, anchor="center")

# Initializes text area for user input
entry = tk.Entry(main_frame, width=35, justify="center")
entry.place(relx=0.5, rely=0.58, anchor="center")

# Initializes submission button
enter_button = tk.Button(main_frame, text="Enter", width=17, height=3, command=get_entry)
enter_button.place(relx=0.5, rely=0.68, anchor="center")

root.eval("tk::PlaceWindow . center")
root.mainloop()
