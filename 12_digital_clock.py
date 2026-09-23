import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%A, %d %B %Y")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")
root.resizable(False, False)

clock_label = tk.Label(root, font=("Courier", 45, "bold"), bg="black", fg="#00FF00")
clock_label.pack(pady=(30, 5))

date_label = tk.Label(root, font=("Courier", 16), bg="black", fg="#00FF00")
date_label.pack()

update_time()

root.mainloop()