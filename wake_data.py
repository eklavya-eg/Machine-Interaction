import sounddevice as sd
from scipy.io.wavfile import write
import os

try:
    os.mkdir("audio_data")
except FileExistsError:
    pass

def record_audio_and_save(save_path, n_times=25):
    input("To start recording Wake Word press Enter: ")
    for i in range(n_times):
        fs = 44100
        seconds = 2

        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(save_path + str(i) + ".wav", fs, myrecording)
        input(f"Press to record next or two stop press ctrl + C ({i + 1}/{n_times}): ")

print("Recording the Wake Word:\n")
record_audio_and_save("audio_data/", n_times=25) 