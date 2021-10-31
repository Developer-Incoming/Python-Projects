import time

import pygame
from pygame import USEREVENT
from pygame import mixer
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name

def play(path, volume, loopFor, cooldown):
    mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")

    mixer.music.load(path)
    mixer.music.set_volume(volume)
    for i in range(loopFor):
        mixer.music.play()
        while mixer.music.get_busy():
            pass
        time.sleep(cooldown)
    mixer.music.unload()

play("audio.mp3", 0.25, 3, 2)
