import tkinter as tk
from tkinter import messagebox
import re

root = tk.Tk()
root.title("Password Checker")

def check_strength():
    password = entry.get()
    strength = "Weak"
    color = "red"
    
    if len(password) >= 8:
        if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password):
            strength = "Strong"
            color = "green"
        elif re.search("[a-z]", password) or re.search("[A-Z]", password):
            strength = "Moderate"
            color = "orange"
            
    result_label.config(text=f"Strength: {strength}", fg=color)

# Widgets
label = tk.Label(root, text="Enter Password:")
label.pack()
entry = tk.Entry(root, show="*") # Mask password
entry.pack()

check_button = tk.Button(root, text="Check", command=check_strength)
check_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
