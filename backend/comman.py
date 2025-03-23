import pyttsx3
import speech_recognition as sr


def Speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 174) 
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def TakeCommand():

    T = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        T.pause_threshold = 1
        T.adjust_for_ambient_noise(source)

        audio = T.listen(source, 10, 6)

    try:
        print("Recognizing...")
        query = T.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


text = TakeCommand()
Speak(text)