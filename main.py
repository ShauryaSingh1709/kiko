import threading
from wake_word import listen_for_wake_word, stop_listening, resume_listening
from speech_to_text import transcribe_audio
from ai_response import get_response
from tts import speak
from weatherapi import get_weather
from music import play_song, pause_song, resume_song, stop_song

def main():
    print("🟢 Kiko is active. Say 'Kiko' to talk...")

    while True:
        if listen_for_wake_word():
            speak("Hello")
            user_input = transcribe_audio()
            print(f"You said: {user_input}")

            if not user_input.strip():
                speak("Sorry, I didn't catch that. Please try again.")
                continue

            user_input_lower = user_input.lower()

            # --- MUSIC CONTROLS ---
            if "pause" in user_input_lower or "ruk jao" in user_input_lower:
                stop_listening()  # Temporarily stop listening for wake word
                pause_song()
                speak("Music paused.")
                resume_listening()  # Resume listening after action

            elif "resume" in user_input_lower or "wapas bajao" in user_input_lower:
                stop_listening()  # Temporarily stop listening for wake word
                resume_song()
                speak("Music resumed.")
                resume_listening()  # Resume listening after action

            elif "stop" in user_input_lower or "band kar do" in user_input_lower:
                stop_listening()  # Temporarily stop listening for wake word
                stop_song()
                speak("Music stopped.")
                resume_listening()  # Resume listening after action

            elif "play" in user_input_lower or "song sunao" in user_input_lower or "gaana bajao" in user_input_lower:
                stop_listening()  # Temporarily stop listening for wake word
                song_name = user_input_lower.replace("play", "").replace("song", "").replace("sunao", "").replace("gaana", "").strip()

                if not song_name:
                    speak("Which song would you like me to play?")
                    song_name = transcribe_audio()

                if not song_name.strip():
                    speak("Sorry, I didn't get the song name. Please try again.")
                    continue

                speak(f"Playing {song_name} now...")
                threading.Thread(target=play_song, args=(song_name,)).start()  # Use threading to play song in the background
                resume_listening()  # Resume listening after action

            # --- WEATHER ---
            elif "weather" in user_input_lower:
                stop_listening()  # Temporarily stop listening for wake word
                speak("Please tell me the city name.")
                city = transcribe_audio()
                print(f"You said the city: {city}")

                if not city.strip():
                    speak("I didn't hear the city name. Want to try again?")
                    resume_listening()  # Resume listening after action
                    continue

                weather_info = get_weather(city)
                print(f"Kiko: {weather_info}")
                speak(weather_info)
                resume_listening()  # Resume listening after action

            # --- GENERAL AI ---
            else:
                reply = get_response(user_input)
                if not reply.strip():
                    speak("Sorry, I couldn't think of a response.")
                else:
                    print(f"Kiko: {reply}")
                    speak(reply)

if __name__ == "__main__":
    main()