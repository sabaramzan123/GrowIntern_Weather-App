# GrowIntern_Weather-App
Weather App
This is a simple weather application built using Python and Tkinter for the GUI and the OpenWeatherMap API for fetching real-time weather data.

Features
City Weather Info: Enter any city name to get the current weather condition, temperature, minimum and maximum temperature, pressure, humidity, wind speed, sunrise, and sunset times.
Detailed Queries: Ask for specific weather details such as min temp, max temp, pressure, humidity, wind speed, sunrise, or sunset times by entering a query.
Usage
Obtain an API key from OpenWeatherMap.
Replace YOUR_API_KEY in the getWeather function with your OpenWeatherMap API key.
Code Overview
The application consists of the following main functions:

getWeather(event=None): Fetches the weather data for the city entered by the user and updates the GUI with the weather information.
getDetail(event=None): Fetches specific weather details based on the user's query and updates the GUI with the requested detail.
GUI Setup
The GUI is set up using Tkinter and includes:

An entry field for the user to input a city name.
Labels to display the weather information.
An entry field for the user to input a specific weather detail query.
Labels to display the specific weather details.
Example
Here's a brief overview of what the app does:

Enter a city name and press Enter to get the weather information.
Enter a specific detail query (e.g., min_temp, max_temp, pressure, humidity, wind, sunrise, sunset) and press Enter to get the specific weather detail.
Screenshots

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
Acknowledgements
OpenWeatherMap for providing the weather API.
