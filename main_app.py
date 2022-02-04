from gpiozero import Button
import speech_recognition as sr
from gtts import gTTS
import pygame # Audio mixer
import random
import os
import vlc
import numpy as np
import time

button = Button(17)
language = 'fr'



class person:
    name = ''
    def setName(self, name):
        self.name = name

# Check for multiple sentences triggering the same answer
def there_exists(terms):
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
    with sr.Microphone() as source:  
        pi_ear.adjust_for_ambient_noise(source, duration=0.5)
        pi_ear.dynamic_energy_threshold = 3000
        play("J'écoute")
        time.sleep(0.5)
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
''''
def play_video(link):
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(link)

    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video file")

    # Read until video is completed
    while(cap.isOpened()):
        
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
'''

def play_vlc(link):
    media_player = vlc.MediaPlayer()
    media = vlc.Media(link)
    media_player.set_media(media)
    media_player.video_set_scale(0.6)
    media_player.play()
    global mediaPlay
    mediaPlay = True

def respond(response):

    # greetings
    global mediaPlay
    if there_exists(['bonjour', "salut", "hey"]):
        play("Bonjour chers visiteurs, bienvenue au Musée de Minéralogie.")
        play_vlc("/home/pi/Desktop/Video Musée/Video intro.mp4")
        mediaPlay = False
        play("Voulez-vous voir la vidéo sur l'histoire du musée ou sur la sépiolite ? ")

    if there_exists(['sépiolite']):
        play("Voici la vidéo sur la sépiolite")
        play_vlc("/home/pi/Desktop/Video Musée/Sépiolite.mp4")
        mediaPlay = False
        play("Voulez-vous voir la vidéo sur l'histoire du musée ou sur la sépiolite ? ")

    if there_exists(['histoire', 'musée']):
        play("Voici la vidéo sur l'histoire du musée")
        play_vlc("/home/pi/Desktop/Video Musée/histoire.mp4")
        mediaPlay = False
        play("Voulez-vous voir la vidéo sur l'histoire du musée ou sur la sépiolite ? ")

    # au revoir 
    if there_exists(["stop", "au revoir", "non merci"]):
        play("Merci et à bientôt")
        exit()

person_obj = person()
while True:
    button.wait_for_press()
    if mediaPlay == False:
        response = record_audio()
        respond(response)



