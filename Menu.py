import tkinter as tk
import Data
import Weather


def get_entry():
    user_input = entry.get()
    entry.delete(0, tk.END)

    data = Data.obtain_data(user_input)
    if data is None:
        error_window = tk.Toplevel(root, width=250, height=300, bg="red")
        error_window.title("Error")

        error_label = tk.Label(error_window, text="Invalid city name", bg="red", fg="white",
                               font=("TkHeaderFont", 20))
        error_label.place(relx=0.5, rely=0.5, anchor="center")
    else:
        Weather.determine_weather(root, data, user_input)


root = tk.Tk()
root.title("Weather Teller")

main_frame = tk.Frame(root, width=500, height=600, bg="#3d6466")
main_frame.grid(row=0, column=0)
main_frame.pack_propagate(False)

title_label = tk.Label(main_frame, text="Weather Teller", bg="#3d6466", fg="white", font=("TkMenuFont", 24))
title_label.place(relx=0.5, rely=0.3, anchor="center")

instruction_label = tk.Label(main_frame, text="Please Enter a City", bg="#3d6466", fg="white",
                             font=("TkHeaderFont", 12))
instruction_label.place(relx=0.5, rely=0.375, anchor="center")

entry = tk.Entry(main_frame, width=35, justify="center")
entry.place(relx=0.5, rely=0.5, anchor="center")

enter_button = tk.Button(main_frame, text="Enter", width=17, height=3, command=get_entry)
enter_button.place(relx=0.5, rely=0.6, anchor="center")

root.eval("tk::PlaceWindow . center")
root.mainloop()
