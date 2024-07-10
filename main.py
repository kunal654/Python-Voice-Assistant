import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import random

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "I did not understand"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "Request error"

# Function to speak
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to open websites
def open_website(url):
    webbrowser.open(url)

# Function to get current time
def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

# Function to open applications
def open_application(application_name):
    if "chrome" in application_name:
        os.system("start chrome")
    elif "notepad" in application_name:
        os.system("start notepad")
    # Add more applications as needed

# Function to handle Jarvis commands
def handle_commands(command):
    if "hello" in command:
        greetings = ["Hello, sir.", "Hi there!", "Hello! How can I help you?"]
        speak(random.choice(greetings))
    elif "time" in command:
        get_time()
    elif "open youtube" in command:
        speak("Opening YouTube")
        open_website("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google")
        open_website("https://www.google.com")
    elif "open github" in command:
        speak("Opening GitHub")
        open_website("https://github.com/kunal654")  
    elif "open linkedin" in command:
        speak("Opening Linkedin")
        open_website("https://linkedin.com/in/kunal-gautam-2981b2292/")
    elif "open" in command and ("chrome" in command or "notepad" in command):
        speak(f"Opening {command.split('open ')[-1]}")
        open_application(command)
    elif "exit" in command or "quit" in command or "stop" in command or "wait" in command:
        speak("Goodbye Kunal !")
        return False
    else:
        speak("I'm sorry, I didn't quite catch that.")

    return True

if __name__ == "__main__":
    speak("Initializing Kunal. How can I assist you today?")
    
    while True:
        command = listen()
        if handle_commands(command):
            continue
        else:
            break
