import os
from backend.comman import Speak
from playsound import playsound
import eel
from backend.config import ASSISTANT_NAME

#playing assistent sound function
def PlayAssistantSound():
    music_dir = "frontend\\files\\audio_file\\mixkit-high-tech-bleep-2521.wav"
    playsound(music_dir)

@eel.expose
def ClickSound():
    music_dir = "frontend\\files\\audio_file\\mixkit-select-click-1109.wav"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        Speak("opening"+query)
        os.system("start "+query)
    else:
        Speak("not found")