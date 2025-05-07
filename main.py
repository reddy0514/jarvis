import os
import eel
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *

def start():
    eel.init("frontend")

    play_assistant_sound()

    @eel.expose
    def init():
        eel.hideLoader()
        speak("Welcome to Jarvis")
        speak("Ready for Face Authentication")
        
        flag = AuthenticateFace()  # Correct function call
        
        if flag == 1:
            speak("Face recognized successfully")
            eel.hideFaceAuth()
            eel.hideFaceAuthSuccess()
            speak("Welcome to Your Assistant Praneeth")
            eel.hideStart()
            play_assistant_sound()
        else:
            speak("Face not recognized. Please try again")

    eel.start("index.html", mode="chrome", host="localhost", block=True)  # Removed manual Edge launch

