import speech_recognition as sr
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import re

class commands:
    level = '\d{1}|\d{2}|\d{3}'

    def __init__(self, model):
        outputs = str(model(self.takeCommand()))
        print(outputs)
        try:
            level = max(re.findall(self.level, outputs), key=len)
            self.set_volume(0.8)
        except Exception as e:
            print(e)

    def set_volume(volume):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_object = cast(interface, POINTER(IAudioEndpointVolume))
        volume_object.SetMasterVolumeLevelScalar(volume, None)

    def takeCommand():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")  
            return "None"
        return query