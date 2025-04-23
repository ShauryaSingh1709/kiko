from gtts import gTTS
import os
import tempfile
import playsound  # pip install playsound==1.2.2

def speak(text):
    tts = gTTS(text=text, lang='hi')  # Use Hindi voice
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        temp_path = fp.name
        tts.save(temp_path)
    playsound.playsound(temp_path)
    os.remove(temp_path)