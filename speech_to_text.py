import speech_recognition as sr

def transcribe_audio():
    recognizer = sr.Recognizer()
    
    # Ensure the microphone is available
    mic_list = sr.Microphone.list_microphone_names()
    if not mic_list:
        print("❌ No microphones found.")
        return ""

    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")

            # Reduce ambient noise (optional, can help improve accuracy)
            recognizer.adjust_for_ambient_noise(source, duration=1)

            # Listen with timeout and phrase limit
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

    except sr.WaitTimeoutError:
        print("⏱️ Listening timed out. No speech detected.")
        return ""
    except Exception as e:
        print(f"⚠️ Mic access error: {e}")
        return ""

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        return text
    except sr.UnknownValueError:
        print("❌ Couldn't understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"🚫 Speech recognition error: {e}") 
        return ""