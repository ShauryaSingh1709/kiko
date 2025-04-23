from speech_to_text import transcribe_audio

# List of wake words Kiko should listen for
wake_words = ["kiko", "keco", "keeko", "keyco", "babu", "Bella", "kiko."]

# Flag to manage the listening state
is_listening = True

def listen_for_wake_word():
    global is_listening
    if not is_listening:
        return False

    print("👂 Listening for wake word...")

    # Continuously listen for wake word
    while is_listening:
        text = transcribe_audio()

        if text:
            print(f"🗣 Heard: {text}")
            if any(word in text.lower() for word in wake_words):
                return True

    return False

def stop_listening():
    """Disable the listening for wake words temporarily."""
    global is_listening
    is_listening = False
    print("⛔️ Kiko is no longer listening for the wake word.")

def resume_listening():
    """Re-enable the listening for wake words."""
    global is_listening
    is_listening = True
    print("🟢 Kiko is now listening for the wake word.")