import tkinter as tk
import Weather


def get_entry():
    user_input = entry.get()
    entry.delete(0, tk.END)
    Weather.determine_weather(user_input)


root = tk.Tk()
root.title("Weather Teller")

frame1 = tk.Frame(root, width=500, height=600, bg="#3d6466")
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

title_label = tk.Label(frame1, text="Weather Teller", bg="#3d6466", fg="white", font=("TkMenuFont", 24))
title_label.place(relx=0.5, rely=0.3, anchor="center")

instruction_label = tk.Label(frame1, text="Please Enter a City", bg="#3d6466", fg="white", font=("TkHeaderFont", 12))
instruction_label.place(relx=0.5, rely=0.375, anchor="center")

entry = tk.Entry(frame1, width=35, justify="center")
entry.place(relx=0.5, rely=0.5, anchor="center")

enter_button = tk.Button(frame1, text="Enter", width=17, height=3, command=get_entry)
enter_button.place(relx=0.5, rely=0.6, anchor="center")

root.eval("tk::PlaceWindow . center")
root.mainloop()
