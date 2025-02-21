import requests
import sys  # Ensure sys is imported

# Replace with your actual API key from OpenWeatherMap
API_KEY = "YOUR_API_KEY"  # <-- Replace this with your real API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a given city"""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"🌍 City: {city}")
        print(f"🌦️ Weather: {weather_desc}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind_speed} m/s")
    else:
        print("❌ City not found! Please check the name.")

# Run script with a city name
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
    else:
        city_name = " ".join(sys.argv[1:])
        get_weather(city_name)
