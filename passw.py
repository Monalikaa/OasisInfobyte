import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

def generate_password():
    total_length = int(length_var.get())

    lower_flag = lower_var.get()
    upper_flag = upper_var.get()
    digit_flag = digit_var.get()
    symbol_flag = symbol_var.get()

    characters = ""
    if lower_flag:
        characters += string.ascii_lowercase
    if upper_flag:
        characters += string.ascii_uppercase
    if digit_flag:
        characters += string.digits
    if symbol_flag:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    complexity_score = complexity_var.get()
    if complexity_score == "Low":
        min_types_required = 2
    elif complexity_score == "Medium":
        min_types_required = 3
    else:
        min_types_required = 4

    selected_types = sum([lower_flag, upper_flag, digit_flag, symbol_flag])

    if selected_types < min_types_required:
        messagebox.showerror("Error", f"Please select at least {min_types_required} types of characters for better complexity.")
        return

    password = ''.join(random.choice(characters) for _ in range(total_length))

    pyperclip.copy(password)  # Copy password to clipboard
    password_entry.config(state=tk.NORMAL)  # Enable editing
    password_entry.delete(0, tk.END)  # Clear any previous content
    password_entry.insert(0, password)  # Display generated password
    password_entry.config(state=tk.DISABLED)  # Disable editing

    messagebox.showinfo("Password Generated", f"Password generated and copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

length_label = tk.Label(frame, text="Total Length of Password:")
length_label.grid(row=0, column=0, sticky="w")

length_var = tk.StringVar()
length_entry = tk.Entry(frame, textvariable=length_var, width=20)
length_entry.grid(row=0, column=1, padx=10)

lower_var = tk.BooleanVar()
lower_checkbutton = tk.Checkbutton(frame, text="Lowercase", variable=lower_var)
lower_checkbutton.grid(row=1, column=0, sticky="w")

upper_var = tk.BooleanVar()
upper_checkbutton = tk.Checkbutton(frame, text="Uppercase", variable=upper_var)
upper_checkbutton.grid(row=2, column=0, sticky="w")

digit_var = tk.BooleanVar()
digit_checkbutton = tk.Checkbutton(frame, text="Digits", variable=digit_var)
digit_checkbutton.grid(row=3, column=0, sticky="w")

symbol_var = tk.BooleanVar()
symbol_checkbutton = tk.Checkbutton(frame, text="Symbols", variable=symbol_var)
symbol_checkbutton.grid(row=4, column=0, sticky="w")

complexity_label = tk.Label(frame, text="Password Complexity:")
complexity_label.grid(row=5, column=0, pady=(10, 0), sticky="w")

complexity_var = tk.StringVar()
complexity_var.set("Low")  # Default value

complexity_options = ["Low", "Medium", "High"]
complexity_dropdown = tk.OptionMenu(frame, complexity_var, *complexity_options)
complexity_dropdown.grid(row=5, column=1, columnspan=3, sticky="ew")

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_entry = tk.Entry(root, show="", width=30, state=tk.DISABLED)  # Entry to display generated password
password_entry.pack(pady=10)

root.mainloop()
