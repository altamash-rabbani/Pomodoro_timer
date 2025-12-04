import tkinter as tk
from tkinter import messagebox
import winsound  # For sound alert on Windows

# Main window
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("500x300")
root.configure(bg="#F6F6F6")

# Variables
counter = 0
running = False
alert_time = 25 * 60  # 25 minutes in seconds

# Title
title_label = tk.Label(
    root,
    text="POMODORO TIMER",
    bg="#F6F6F6",
    fg="#282828",
    font=("Helvetica", 23, "bold")
)
title_label.pack(pady=10)

# Timer Label
label = tk.Label(root, text="00:00", font=("Arial", 50), bg="#F6F6F6", fg="#17541D")
label.pack(pady=20)

# Functions
def update_timer():
    global counter, running
    if running:
        mins, secs = divmod(counter, 60)
        label.config(text=f"{mins:02d}:{secs:02d}")
        counter += 1
        
        # Alert when 25 minutes reached
        if counter == alert_time:
            running = False  # stop timer
            messagebox.showinfo("Pomodoro Complete!", "Time's up! Take a break.")
            label.config(text=f"00:00")
            counter=0
            # if winsound fails on non-Windows systems
        
        root.after(1000, update_timer)

def start():
    global running
    if not running:
        running = True
        update_timer()

def stop():
    global running
    running = False

def reset():
    global counter, running
    running = False
    counter = 0
    label.config(text="00:00")

# Buttons
tk.Button(root, text="START", bg="#17541D", fg="#FFFFFF", width=10, height=2, command=start).place(x=80, y=200)
tk.Button(root, text="STOP", bg="#17541D", fg="#FFFFFF", width=10, height=2, command=stop).place(x=210, y=200)
tk.Button(root, text="RESET", bg="#17541D", fg="#FFFFFF", width=10, height=2, command=reset).place(x=350, y=200)

root.mainloop()
