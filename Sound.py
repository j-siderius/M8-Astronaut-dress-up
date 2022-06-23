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
        pygame.mixer.set_num_channels(4)
        self.launch = pygame.mixer.Channel(1)
        self.timer = 0
        self.frameCount = 0

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

    def launching(self):
        if self.launch.get_busy():
            self.countdownlaunchSound.stop()
        self.launch.play(self.countdownlaunchSound)

    def getFrameCount(self, frameCount):
        self.frameCount = frameCount

    '''    
    def timeElapsed(self, time):
        onlyOnce = True
        prevTime = 0
        if onlyOnce:
            prevTime = self.frameCount
            onlyOnce = False
        if  self.frameCount == prevTime + time:
            return True
    '''
