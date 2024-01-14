from tkinter import *
import requests
from datetime import datetime

root = Tk()
root.geometry("500x400")
root.title("Weather App")

city_value = StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def get_weather(city):
    api_key = "ad903ae75fcc38ac3a6a4455f7d64687"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def show_weather():
    city_name = city_value.get()
    weather_data = get_weather(city_name)

    if weather_data['cod'] == 200:
        kelvin = 273
        temp = int(weather_data['main']['temp'] - kelvin)
        feels_like_temp = int(weather_data['main']['feels_like'] - kelvin)
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        sunrise = weather_data['sys']['sunrise']
        sunset = weather_data['sys']['sunset']
        timezone = weather_data['timezone']
        cloudy = weather_data['clouds']['all']
        description = weather_data['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        weather_icon = weather_data['weather'][0]['icon']

        weather_details = (
            f"Weather of: {city_name}\n"
            f"Temperature: {temp}°C\n"
            f"Feels like: {feels_like_temp}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Sunrise at {sunrise_time} and Sunset at {sunset_time}\n"
            f"Cloud: {cloudy}%\nInfo: {description}"
        )
        
        tfield.delete("1.0", "end")
        tfield.insert(INSERT, weather_details)

        # Retrieve weather icon
        weather_icon_url = f"http://openweathermap.org/img/w/{weather_icon}.png"
        response = requests.get(weather_icon_url)
        img_data = response.content
        with open("weather_icon.png", "wb") as img_file:
            img_file.write(img_data)

        img = PhotoImage(file="weather_icon.png")
        icon_label.config(image=img)
        icon_label.image = img
        icon_label.pack()
    else:
        tfield.delete("1.0", "end")
        tfield.insert(INSERT, f"Weather for '{city_name}' not found!\nKindly Enter a valid City Name !!")

city_label = Label(root, text='Enter City Name', font='Arial 12 bold')
city_label.pack(pady=10)

inp_city = Entry(root, textvariable=city_value, width=24, font='Arial 14 bold')
inp_city.pack()

show_weather_btn = Button(root, command=show_weather, text="Check Weather", font="Arial 10", bg='lightblue',
                          fg='black', activebackground="teal", padx=5, pady=5)
show_weather_btn.pack(pady=20)

tfield = Text(root, width=46, height=8)
tfield.pack()

icon_label = Label(root)
icon_label.pack()

root.mainloop()
