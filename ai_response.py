import google.generativeai as genai
from weatherapi import get_weather

genai.configure(api_key="AIzaSyCU4xhPKQsID8ynwRdYpnsb4L4OBQDTuc0")
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def get_response(prompt):
    prompt_lower = prompt.lower()

    if "weather in" in prompt_lower:
        city = prompt_lower.split("weather in")[-1].strip().rstrip("?")
        return get_weather(city)

    elif "who made you" in prompt_lower or "who created you" in prompt_lower:
        return "I am Kiko, your virtual assistant. I was created by Adi and Shaurya."

    elif "who are you" in prompt_lower:
        return "I am Kiko, your friendly AI assistant, built by Adi and Shaurya to help you out."

    response = model.generate_content(prompt)
    return response.text