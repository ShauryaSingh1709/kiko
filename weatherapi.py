# weather.py
import requests

API_KEY = "c7d0c127c439c24a5e2d603729441ea1"  # Your OpenWeatherMap API key

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return f"Sorry, I couldn't find the weather for {city}."

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        return (
            f"The weather in {city} is {description} with a temperature of {temp}°C, "
            f"humidity at {humidity}%, and wind speed of {wind} meters per second."
        )

    except Exception as e:
        return "Oops! I ran into an issue fetching the weather."