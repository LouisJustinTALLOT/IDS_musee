import time
import speech_recognition as sr

def callback(recognizer, audio):
    print(recognizer.recognize_google(audio))

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    recognizer.adjust_for_ambient_noise(source)

stop_listening = recognizer.listen_in_background(mic, callback)

for i in range(50):
    print("Hello")
    time.sleep(0.1)

stop_listening()