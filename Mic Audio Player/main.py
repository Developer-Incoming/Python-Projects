import time

import pygame
from pygame import mixer

def play(path, volume, loopFor, cooldown):
    mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")
    mixer.music.load(path)
    mixer.music.set_volume(volume)
    
    if loopFor == 0:
        for i in range(loopFor):
            mixer.music.play()
            while mixer.music.get_busy():
                pass
            time.sleep(cooldown)
    else:
        while True:
            mixer.music.play()
            while mixer.music.get_busy():
                pass
            time.sleep(cooldown)
    
    mixer.music.unload()

play("audio.mp3", 0.5, 3, 2)
