import os
import time
import speech_recognition as sr

def transcribe_audio():
    recognizer = sr.Recognizer()
    audio_path = "/data/data/com.termux/files/home/audio.wav"

    print("🎙️ Recording voice for 5 seconds...")
    os.system(f"termux-microphone-record -l 5 -f {audio_path}")
    time.sleep(6)  # wait till file is saved

    if not os.path.exists(audio_path):
        print("⚠️ Audio file not recorded.")
        return ""

    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="hi-IN")
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Couldn't understand.")
        return ""
    except sr.RequestError as e:
        print(f"🚫 Recognition error: {e}")
        return ""
    finally:
        os.remove(audio_path)