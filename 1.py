import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import pywhatkit
import pyautogui
import pyjokes

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Fix: Correct voice property setting


def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listens to user input and returns the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        speak("Sorry, I didn't understand.")
        return None
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        speak("Could not request results, check your internet connection.")
        return None

    return query.lower()


def wake_up():
    """Waits for the wake-up command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Assistant is sleeping... Say 'wake up' to activate.")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None

    return query.lower()


def wish():
    """Greets the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning, boss.")
    elif 12 <= hour < 17:
        speak("Good afternoon, boss.")
    elif 17 <= hour < 21:
        speak("Good evening, boss.")
    else:
        speak("Good night, boss.")


def search_wikipedia(query):
    """Searches Wikipedia and returns the summary."""
    speak("Searching Wikipedia...")
    try:
        results = wikipedia.summary(query, sentences=1)
        speak(f"According to Wikipedia, {results}")
        print(results)
    except:
        speak("No results found.")


def open_youtube():
    """Opens YouTube and plays a song."""
    speak("Opening YouTube.")
    pywhatkit.playonyt("arabic kuthu")  # Change to a default song or accept input


def tell_time():
    """Tells the current time."""
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {time_now}")


def open_google():
    """Opens Google Chrome."""
    speak("Opening Google Chrome.")
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    while True:
        search_query = listen()
        if search_query and "search" in search_query:
            search_query = search_query.replace("search", "").strip()
            pyautogui.write(search_query)
            pyautogui.press("enter")
            speak("Searching...")
        elif search_query and ("close chrome" in search_query or "exit chrome" in search_query):
            pyautogui.hotkey("ctrl", "w")
            speak("Closing Google Chrome.")
            break


def tell_joke():
    """Tells a joke."""
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


def open_notepad():
    """Opens Notepad and performs text-related operations."""
    speak("Opening Notepad.")
    os.startfile("C:\\Windows\\System32\\notepad.exe")
    while True:
        notepad_query = listen()
        if notepad_query and "paste" in notepad_query:
            pyautogui.hotkey("ctrl", "v")
        elif notepad_query and "save this file" in notepad_query:
            pyautogui.hotkey("ctrl", "s")
            speak("Sir, please specify a name for this file.")
            file_name = listen()
            pyautogui.write(file_name)
            pyautogui.press("enter")
        elif notepad_query and "type" in notepad_query:
            speak("Please tell me what to write.")
            while True:
                text = listen()
                if text == "exit typing":
                    speak("Done, sir.")
                    break
                elif text:
                    pyautogui.write(text)
        elif notepad_query and ("exit notepad" in notepad_query or "close notepad" in notepad_query):
            speak("Closing Notepad.")
            pyautogui.hotkey("ctrl", "w")
            break


def mute_assistant():
    """Mutes the assistant (stops listening)."""
    speak("I am muting, sir.")
    return False  # Used to break the loop


def exit_program():
    """Exits the program."""
    speak("I am leaving, sir. Bye!")
    quit()


commands_dict = {
    "wikipedia": search_wikipedia,
    "open youtube": open_youtube,
    "time": tell_time,
    "mute": mute_assistant,
    "exit program": exit_program,
    "open google": open_google,
    "open notepad": open_notepad,
    "joke": tell_joke,
    "who is nilesh": lambda: speak("Nilesh is my boss."),
    "who is your boss": lambda: speak("Nilesh is my boss."),
    "what can you do for me": lambda: speak("I can perform tasks through your voice commands."),
    "thank you": lambda: speak("It's my pleasure, sir."),
    "minimize": lambda: (speak("Minimizing."), pyautogui.hotkey("win", "up", "up")),
    "close the window": lambda: (speak("Closing the window."), pyautogui.hotkey("alt", "f4")),
    "screenshot": lambda: (speak("Taking screenshot."), pyautogui.hotkey("ctrl", "prtsc")),
    "pause": lambda: (speak("Pausing."), pyautogui.press("space")),
}


if __name__ == "__main__":
    while True:
        query = wake_up()
        if query and "wake up" in query:
            wish()
            speak("Yes boss, what can I do for you?")
            while True:
                query = listen()
                if query:
                    for key in commands_dict:
                        if key in query:
                            result = commands_dict[key]()
                            if result is False:  # If the function returns False, break the loop
                                break
                            else:
                                continue
