import pygame

class SoundIndex:
    SOUND_DICT = {
        0 : ["sound/normal.mp3", "normal"],
        1 : ["sound/explosion.mp3", "explosion"],
        2 : ["sound/stamp.mp3", "stamp"]
    }

class SoundPlayer:
    def __init__(self):
        self.put_sound = None
        pygame.mixer.init()
    
    def set_sound(self, sound: str):
        self.put_sound = pygame.mixer.Sound(sound)

    def play_sound(self):
        if(self.play_sound != None): pygame.mixer.Sound.play(self.put_sound)