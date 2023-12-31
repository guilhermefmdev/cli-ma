import os
import argparse
import pyfiglet
from simple_chalk import chalk
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_ICONS = {
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

parser = argparse.ArgumentParser(
    description="Check the weather for a certaint country/city")
parser.add_argument(
    "country", help="The country/city to check the weather for")
args = parser.parse_args()
url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information"))
    exit()

data = response.json()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon}  {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

print(chalk.green(output))
