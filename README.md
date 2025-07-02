# Machine Interaction

A Python-based system for hands-free computer interaction using voice commands and hand gestures. This project combines wake word detection, speech recognition, and hand tracking to control system functions such as mouse movement and volume adjustment.

## Features

- **Wake Word Detection:** Listens for a specific wake word using a trained neural network model.
- **Voice Commands:** After activation, recognizes spoken commands to perform actions like adjusting system volume.
- **Hand Gesture Mouse Control:** Uses a webcam and hand tracking to move the mouse cursor and perform left/right clicks with gestures.
- **Real-time Feedback:** Provides audio feedback using text-to-speech.

## Project Structure

```
Machine-Interaction/
  ├── Commands.py         # Handles voice command recognition and system volume control
  ├── Cursor.py           # Implements hand gesture-based mouse control
  ├── main.py             # Entry point: loads models and starts the system
  ├── WakeWord.py         # Wake word detection and command activation logic
  ├── Weights/
  │   └── WWD.h5          # Pre-trained wake word detection model
  └── Docs/
      ├── swot.docx       # Project SWOT analysis (not included in this README)
      └── synopsis-audio.docx # Project synopsis (not included in this README)
```

## Requirements

- Python 3.x
- `speech_recognition`
- `pycaw`
- `comtypes`
- `mediapipe`
- `pyautogui`
- `opencv-python`
- `librosa`
- `numpy`
- `sounddevice`
- `pyttsx3`
- `transformers`
- `tensorflow`

Install dependencies with:
```bash
pip install -r requirements.txt
```
*(You may need to create this file with the above packages.)*

## Usage

1. Place the pre-trained wake word model (`WWD.h5`) in the `Weights/` directory.
2. Run the main script:
   ```bash
   python main.py
   ```
3. The system will start listening for the wake word. Once detected, it will accept voice commands and enable hand gesture mouse control.

## Contributors

- Rishabh Sajwan
- Eklavya Gupta
- Arsh Bansal 