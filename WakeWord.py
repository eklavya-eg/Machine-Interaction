import time
import sounddevice as sd
import librosa
import numpy as np
from threading import Thread, Event
import pyttsx3
from Commands import commands

class WakeWord:
    def __init__(self, model, command_model):
        self.model=model
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        # self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
        self.fs = 22050
        self.seconds = 2
        self.command_model = command_model
        self.command = Event()
        self.command.clear()
        listen_thread = Thread(target=self.listener, name="listener", daemon=True)
        listen_thread.start()
        time.sleep(0.1)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.endLoop()

    def listener(self):
        while True:
            while self.command.is_set():
                print(1)
                time.sleep(0.1)
            myrecording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=1)
            sd.wait()
            mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=self.fs, n_mfcc=40)
            mfcc_processed = np.mean(mfcc.T, axis=0)
            self.prediction_thread(mfcc_processed)
            time.sleep(0.001)

    def prediction(self, y):
        prediction = self.model.predict(np.expand_dims(y, axis=0))
        if prediction[:, 1] > 0.90:
            if self.engine._inLoop:
                self.engine.endLoop()
            self.speak("Yeah Listening")
            self.command.set()
            commands(self.command_model)
            self.command.clear()
            print(2)

    def prediction_thread(self, y):
        pred_thread = Thread(target=self.prediction, name="detector", args=(y,))
        pred_thread.start()