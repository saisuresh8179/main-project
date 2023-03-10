import speech_recognition as sr

def main2():
    # Create a Recognizer object
    r = sr.Recognizer()

    # Use the microphone as a source to capture audio
    with sr.Microphone() as source:
        print("Speak something...")
        # Listen for audio and store it in audio_data variable
        audio_data = r.record(source, duration=5)  # Records for 5 seconds

        # Convert speech to text
        text = r.recognize_google(audio_data)

        # Print the text
        print(f"You said: {text}")
        return text
