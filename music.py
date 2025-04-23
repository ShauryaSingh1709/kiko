import yt_dlp
import os
import tempfile
import subprocess
import threading
from tts import speak

current_song = None
is_playing = False

def play_song(song_name):
    global current_song, is_playing

    if is_playing:
        speak("A song is already playing.")
        return "A song is already playing."

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            ydl_opts = {
                'format': 'bestaudio/best',
                'noplaylist': True,
                'quiet': True,
                'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f"ytsearch1:{song_name}", download=True)
                downloaded_file = ydl.prepare_filename(info['entries'][0]).replace(".webm", ".mp3").replace(".m4a", ".mp3")

            current_song = downloaded_file
            is_playing = True

            song_title = info['entries'][0]['title']
            speak(f"Playing {song_title}")

            subprocess.call(["mpg123", downloaded_file])

            is_playing = False
            speak("Gaana khatam ho gaya")
            current_song = None

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        is_playing = False
        return f"Sorry, I couldn't play '{song_name}'."

def pause_song():
    speak("Pause not supported in this version. Only stop works.")

def resume_song():
    speak("Resume not supported. Please play the song again.")

def stop_song():
    global is_playing
    subprocess.call(["pkill", "mpg123"])
    is_playing = False
    speak("Gaana band ho gaya")