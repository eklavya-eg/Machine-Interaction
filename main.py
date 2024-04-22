from Cursor import Cursor
from WakeWord import WakeWord
from transformers import pipeline
from tensorflow.keras.models import load_model
from threading import Thread

WWD_MODEL_PATH = "Weights/WWD.h5"

model = pipeline("sentiment-analysis")
wwd_model = load_model(WWD_MODEL_PATH)

WakeWord(wwd_model, model)
Cursor.start()
