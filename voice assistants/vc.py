# Import required libraries
import speech_recognition as sr  # To recognize speech
import pyttsx3  # To convert text to speech
import pywhatkit  # To play YouTube videos
import datetime  # To get the current time
import wikipedia  # To search information

# Start the text-to-speech engine
engine = pyttsx3.init()

# Set a female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user
def take_command():
    recognizer = sr.Recognizer()  # Create a recognizer
    with sr.Microphone() as source:  # Use the microphone to listen
        print("Listening...")
        audio = recognizer.listen(source)  # Listen for audio

    try:
        command = recognizer.recognize_google(audio)  # Convert audio to text
        print(f"You said: {command}")
        return command.lower()
    except:
        speak("Sorry, I didn't understand. Please try again.")
        return ""

# Main function to run the assistant
def run_assistant():
    command = take_command()

    # Play a song on YouTube
    if "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)

    # Tell the current time
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}.")

    # Get information from Wikipedia
    elif "who is" in command or "what is" in command:
        query = command.replace("who is", "").replace("what is", "").strip()
        info = wikipedia.summary(query, sentences=1)
        speak(info)

    # Stop the assistant
    elif "stop" in command or "bye" in command or "exit" in command:
        speak("Goodbye! Have a great day!")
        exit()

    # When the command is not understood
    else:
        speak("I didn't get that. Please try again.")

# Start the assistant
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")
    print("Enter choice: 1 for speaking, 2 to exit program")
    ch=1
    while True:
        ch=int(input("Your choice: "))
        if (ch==1):
            run_assistant()
        elif (ch==2):
            break
        else:
            print("Choice mismatched! Try again.")
