"""
This class will handle the audio coming from python
"""
import pygame
from pygame import mixer
import time


class Sound:

    def __init__(self):
        "Insert stuff"
        pygame.mixer.init()
        self.audioSetup()
        self.timer = 0

    def audioSetup(self):
        """
        This function will setup the audio
        """
        self.selectSound = pygame.mixer.Sound('Planet select.wav')
        self.countdownlaunchSound = pygame.mixer.Sound('Countdown launch.wav')
        self.buzzerSound = pygame.mixer.Sound('Buzzer.wav')
        self.heartbeepSound = pygame.mixer.Sound('Heartbeep.wav')
        self.heartbeeplongSound = pygame.mixer.Sound('Heartbeep long.wav')
        self.noiseSound = pygame.mixer.Sound('Space Noise.wav')

        self.spaceMusic = pygame.mixer.Sound('Space music.mp3')
        self.earthMusic = pygame.mixer.Sound('Earth music.mp3')

    def mixer(self):
        """
        This function will handle the sounds and when they should be played
        """
        self.launchSound.play()
        time.sleep(5)
        self.launchSound.stop()
        time.sleep(2)
        self.launchSound.play()
        time.sleep(3)
        self.spaceMusic.stop()
        time.sleep(4)

    def launchSound(self):


        '''
            laser = Sound()

            if __name__ == '__main__':
                laser.mixer()
        '''
