import os
import time

from gtts import gTTS

import pygame
from pygame import USEREVENT
from pygame import mixer
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name

language = input("Language [en, ar... etc]:\n")
accent = input("Accent: [com.au, co.uk, com, ca, co.in, ie, co.za, ca, fr, com.br, pt, com.mx, es]:\n")

if accent == "":
    accent = "com"
os.system("cls")
os.system("title Google Text-to-Speech")

def main():
    mytext = input("Message: ")
    myobj = gTTS(text=mytext, tld=accent, lang=language)
    myobj.save("voice.mp3")

    mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")

    mixer.music.load("voice.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.music.unload()
    os.remove("voice.mp3")
    os.system("cls")

while True:
    main()
