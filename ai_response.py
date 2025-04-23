import requests
import json
from weatherapi import get_weather

API_KEY = "AIzaSyCU4xhPKQsID8ynwRdYpnsb4L4OBQDTuc0"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

def get_response(prompt):
    prompt_lower = prompt.lower()

    if "weather in" in prompt_lower:
        city = prompt_lower.split("weather in")[-1].strip().rstrip("?")
        return get_weather(city)

    elif "who made you" in prompt_lower or "who created you" in prompt_lower:
        return "I am Kiko, your virtual assistant. I was created by Adi and Shaurya."

    elif "who are you" in prompt_lower:
        return "I am Kiko, your friendly AI assistant, built by Adi and Shaurya to help you out."

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error: {e}"