import yt_dlp
import os
import tempfile
import pygame
import threading
import time
from tts import speak

current_song = None
is_paused = False
is_playing = False  # Flag to check if a song is currently playing

def play_song(song_name):
    global current_song, is_paused, is_playing
    if is_playing:  # Prevent playing a new song if one is already playing
        speak("A song is already playing.")
        return "A song is already playing."

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            ffmpeg_path = r"C:\Path(of hehe)"  # Replace with your path
            ydl_opts = {
                'format': 'bestaudio/best',
                'noplaylist': True,
                'quiet': True,
                'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
                'ffmpeg_location': ffmpeg_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f"ytsearch1:{song_name}", download=True)
                downloaded_file = ydl.prepare_filename(info['entries'][0]).replace(".webm", ".mp3").replace(".m4a", ".mp3")

            song_title = info['entries'][0]['title']
            current_song = downloaded_file
            is_paused = False
            is_playing = True

            pygame.mixer.init()
            pygame.mixer.music.load(downloaded_file)
            pygame.mixer.music.play()

            speak(f"Playing {song_title}")

            # Wait until the song is done playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_playing = False
            speak("Gaana khatam ho gaya")
            current_song = None
            return f"Finished playing {song_title}"

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        is_playing = False
        return f"Sorry, I couldn't play '{song_name}'."

def pause_song():
    global is_paused
    if pygame.mixer.music.get_busy() and not is_paused:
        pygame.mixer.music.pause()
        is_paused = True
        speak("Gaana ruk gaya")

def resume_song():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
        speak("Wapas baj raha hai")

def stop_song():
    global is_paused, current_song, is_playing
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        is_paused = False
        is_playing = False
        current_song = None
        speak("Gaana band ho gaya")