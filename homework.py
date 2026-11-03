from tkinter import *

from tkinter import messagebox

import time

root = Tk()

root.geometry("300x300")

root.title("Egg Timer")

def start_timer(seconds):
    update_timer(seconds)

def update_timer(seconds):
    mins, secs = divmod(seconds, 60)
    time_format = f"{mins:02d}:{secs:02d}"
    time_label.config(text = time_format)
    if seconds > 0:
        root.after(1000, update_timer, seconds - 1)
    else:
        time_label.config(text = "DONE!")

def soft_boiled():
    start_timer(3*60)

def medium_boiled():
    start_timer(5*60)

def hard_boiled():
    start_timer(10*60)

time_label = Label(root, text = "00:00", font = ("Arial", 30))
time_label.place(x = 70, y = 30)

submit1Button = Button(root, text = "3 min", command = soft_boiled)
submit1Button.place(x = 105, y = 100)

submit2Button = Button(root, text = "5 min", command = medium_boiled)
submit2Button.place(x = 105, y = 150)

submit3Button = Button(root, text = "10 min", command = hard_boiled)
submit3Button.place(x = 105, y = 200)

root.mainloop()