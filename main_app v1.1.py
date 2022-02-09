import speech_recognition as sr
from gtts import gTTS
import pygame # Audio mixer
import random
import os
import vlc
import numpy as np
import time

language = 'fr'
mic = sr.Microphone()



class person:
    name = ''
    def setName(self, name):
        self.name = name

# Check for multiple sentences triggering the same answer
def there_exists(terms,response):
    for term in terms:
        if term in response:
            return True

# initialise a recogniser
pi_ear = sr.Recognizer()
mediaPlay = False



# Playing the converted file
def play(mytext):
    myobj = gTTS(text=mytext, lang='fr', slow=False)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    myobj.save(audio_file)
    print(f"bot: {mytext}") # print what app said
    # play the audio file
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    os.remove(audio_file) # remove audio file

def record_audio():
        audio = pi_ear.listen(source, timeout=1.0)
        response = ''
        try:
            response = pi_ear.recognize_google(audio, language="fr-FR")
        except sr.UnknownValueError:
            play("Je ne comprends pas")
        except sr.RequestError:
            play("Désolé, le service n'est pas disponible")
        print(f">> {response.lower()}") # print what user said
        return response.lower()

def respond(response):

    # greetings
    global mediaPlay
    if there_exists(["présentation", "vidéo de présentation", "introduction", "présentation", "présentation générale", "présentation générale du musée"], response):
        play("Bonjour chers visiteurs, bienvenue au Musée de Minéralogie.")
        #### Launch video

    if there_exists(['sépiolite', "présentation de la sépiolite"], response):
        play("Voici la vidéo sur la sépiolite")
        #### Launch video

    if there_exists(['histoire', 'musée',"histoire du musée et de l'école", "histoire de l'école", "vidéo sur l'histoire"], response):
        play("Voici la vidéo sur l'histoire du musée")
        #### Launch video

    if there_exists(['calcite', "présentation de la calcite"], response):
        play("Voici la vidéo sur la calcite")
        #### Launch video

    if there_exists(['azurite', "présentation de la azurite"], response):
        play("Voici la vidéo sur la azurite")
        #### Launch video


#####


with mic as source:  
    pi_ear.adjust_for_ambient_noise(source, duration=0.5)
    pi_ear.dynamic_energy_threshold = 3000

def detectHello(recognizer, audio):
    response = recognizer.recognize_google(audio, language="fr-FR")
    print(response)
    respond(response)

stop_listening = pi_ear.listen_in_background(mic, detectHello)

while True:
    pass