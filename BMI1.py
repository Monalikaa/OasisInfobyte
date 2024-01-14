import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate BMI
def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # Convert height to meters
    bmi = round(weight / (height ** 2), 2)
    bmi_result_label.config(text=f"Your BMI is: {bmi}")

    # Determine BMI category
    if bmi < 16:
        bmi_category_label.config(text="You are very underweight.", fg='red', font=('Arial', 12, 'bold'))
    elif 16 <= bmi < 18.5:
        bmi_category_label.config(text="You are underweight.", fg='orange', font=('Arial', 12, 'bold'))
    elif 18.5 <= bmi <= 24:
        bmi_category_label.config(text="Congratulations! You have a healthy weight.", fg='green', font=('Arial', 12, 'bold'))
    elif 25 <= bmi < 30:
        bmi_category_label.config(text="You are Overweight.", fg='orange', font=('Arial', 12, 'bold'))
    else:
        bmi_category_label.config(text="You are Obese.", fg='red', font=('Arial', 12, 'bold'))

    save_user_data(weight, height, bmi)  # Save user data for historical analysis

# Function to save user data for historical analysis
def save_user_data(weight, height, bmi):
    user_data.append((weight, height, bmi))

# Function to show historical BMI data
def show_historical_data():
    history_window = tk.Toplevel(root)
    history_window.title("Historical BMI Data")

    history_label = tk.Label(history_window, text="Historical BMI Data", font=('Arial', 14, 'bold'))
    history_label.pack()

    if not user_data:
        tk.Label(history_window, text="No historical data available.", font=('Arial', 12)).pack()
    else:
        for idx, (weight, height, bmi) in enumerate(user_data, start=1):
            data_label = tk.Label(
                history_window,
                text=f"Entry {idx}: Weight: {weight} kg, Height: {height} cm, BMI: {bmi}",
                font=('Arial', 12)
            )
            data_label.pack(pady=5)

# Function to show BMI trend analysis
def show_bmi_trend():
    bmi_data = [data[2] for data in user_data]  # Extract BMI data for trend analysis
    if len(bmi_data) > 1:
        plt.plot(np.arange(1, len(bmi_data) + 1), bmi_data, marker='o', linestyle='-')
        plt.xlabel('Entries')
        plt.ylabel('BMI')
        plt.title('BMI Trend Analysis')
        plt.show()
    else:
        messagebox.showinfo("Information", "Insufficient data to show BMI trend.")

# GUI setup
root = tk.Tk()
root.title("BMI Calculator and Analysis")

user_data = []  # List to store user data (weight, height, BMI)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

weight_label = tk.Label(frame, text="Enter your weight (kg):", font=('Arial', 12))
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(frame, font=('Arial', 12))
weight_entry.grid(row=0, column=1)

height_label = tk.Label(frame, text="Enter your height (cm):", font=('Arial', 12))
height_label.grid(row=1, column=0)

height_entry = tk.Entry(frame, font=('Arial', 12))
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi, font=('Arial', 12))
calculate_button.grid(row=2, columnspan=2, pady=10)

bmi_result_label = tk.Label(frame, text="", font=('Arial', 12))
bmi_result_label.grid(row=3, columnspan=2)

bmi_category_label = tk.Label(frame, text="", font=('Arial', 12))
bmi_category_label.grid(row=4, columnspan=2)

history_button = tk.Button(frame, text="View Historical Data", command=show_historical_data, font=('Arial', 12))
history_button.grid(row=5, columnspan=2, pady=10)

trend_button = tk.Button(frame, text="View BMI Trend", command=show_bmi_trend, font=('Arial', 12))
trend_button.grid(row=6, columnspan=2, pady=10)

root.mainloop()
