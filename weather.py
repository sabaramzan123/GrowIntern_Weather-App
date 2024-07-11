import tkinter as tk
import requests
import time

def getWeather(event=None):
    city = textField.get()
    api_key = "9d52adfb8e7b4f19235c55a5beb269b5"
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        json_data = requests.get(api_url).json()
        if json_data.get('cod') != 200:
            final_info = "City not found!"
            final_data = ""
        else:
            global weather_data
            weather_data = {
                "condition": json_data['weather'][0]['main'],
                "temp": int(json_data['main']['temp'] - 273.15),
                "min_temp": int(json_data['main']['temp_min'] - 273.15),
                "max_temp": int(json_data['main']['temp_max'] - 273.15),
                "pressure": json_data['main']['pressure'],
                "humidity": json_data['main']['humidity'],
                "wind": json_data['wind']['speed'],
                "sunrise": time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600)),
                "sunset": time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
            }
            final_info = f"{weather_data['condition']}\n{weather_data['temp']}°C"
            final_data = (
                f"\nMin Temp: {weather_data['min_temp']}°C\n"
                f"Max Temp: {weather_data['max_temp']}°C\n"
                f"Pressure: {weather_data['pressure']}\n"
                f"Humidity: {weather_data['humidity']}\n"
                f"Wind Speed: {weather_data['wind']}\n"
                f"Sunrise: {weather_data['sunrise']}\n"
                f"Sunset: {weather_data['sunset']}"
            )
    except Exception as e:
        final_info = "Error!"
        final_data = str(e)

    label1.config(text=final_info)
    label2.config(text=final_data)

def getDetail(event=None):
    detail = textField2.get().lower()
    if detail in weather_data:
        label3.config(text=f"{detail.capitalize()}: {weather_data[detail]}")
    else:
        label3.config(text="Detail not found. Please ask for 'min_temp', 'max_temp', 'pressure', 'humidity', 'wind', 'sunrise', or 'sunset'.")

# Set up the GUI
canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title("Weather App")

# Setting the background color
canvas.configure(bg="#1E90FF")

# Fonts
title_font = ("Helvetica", 20, "bold")
info_font = ("Helvetica", 15)
detail_font = ("Helvetica", 12, "italic")

# Text field for city input
textField = tk.Entry(canvas, justify='center', width=20, font=title_font, bg="#ADD8E6", fg="#000000")
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

# Labels to display weather info
label1 = tk.Label(canvas, font=title_font, bg="#1E90FF", fg="#FFFFFF")
label1.pack()
label2 = tk.Label(canvas, font=info_font, bg="#1E90FF", fg="#FFFFFF")
label2.pack()

# Text field for detail input
textField2 = tk.Entry(canvas, justify='center', width=20, font=detail_font, bg="#ADD8E6", fg="#000000")
textField2.pack(pady=20)
textField2.bind('<Return>', getDetail)

# Label to display specific details
label3 = tk.Label(canvas, font=detail_font, bg="#1E90FF", fg="#FFFFFF")
label3.pack()

# Initialize weather data
weather_data = {}

canvas.mainloop()
