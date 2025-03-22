from playsound import playsound
import eel


def PlayAssistantSound():
    music_dir = "frontend\\files\\audio_file\\mixkit-high-tech-bleep-2521.wav"
    playsound(music_dir)

@eel.expose
def ClickSound():
    music_dir = "frontend\\files\\audio_file\\mixkit-select-click-1109.wav"
    playsound(music_dir)