import re
import pyttsx3
import speech_recognition as sr
import eel
import time
import pywhatkit as kit 


def Speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 174) 
    eel.DisplayMessage(text)
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def TakeCommand():

    T = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        T.pause_threshold = 1
        T.adjust_for_ambient_noise(source)

        audio = T.listen(source, 10, 6)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = T.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        # Speak(query)
        

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


# text = TakeCommand()
# Speak(text)

@eel.expose
def AllCommands():

    query = TakeCommand()
    print(query)

    if "open" in query:
        from backend.features import openCommand
        openCommand(query)
    
    elif "on youtube":
        from backend.comman import PlayYouTube
        PlayYouTube(query)
    
    else:
        print("not found")  
    eel.ShowHood()

def PlayYouTube(query):
    search_term = extract_yt_term(query)
    Speak("Playing " + search_term+" in youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None