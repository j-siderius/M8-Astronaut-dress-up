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
        pygame.mixer.set_num_channels(8)
        self.launch = pygame.mixer.Channel(1)
        self.beat = pygame.mixer.Channel(2)
        self.beatLong = pygame.mixer.Channel(3)
        self.earthBackground = pygame.mixer.Channel(4)
        self.timer = 0
        self.frameCount = 0

    def audioSetup(self):
        """
        This function will setup the audio
        """
        self.selectSound = pygame.mixer.Sound('Sounds/Planet select.wav')
        self.countdownlaunchSound = pygame.mixer.Sound('Sounds/Countdown launch.wav')
        self.buzzerSound = pygame.mixer.Sound('Sounds/Buzzer.wav')
        self.heartbeepSound = pygame.mixer.Sound('Sounds/Heartbeep.wav')
        self.heartbeeplongSound = pygame.mixer.Sound('Sounds/Heartbeep long.wav')
        self.noiseSound = pygame.mixer.Sound('Sounds/Space Noise.wav')

        self.spaceMusic = pygame.mixer.Sound('Sounds/Space music.mp3')
        self.earthMusic = pygame.mixer.Sound('Sounds/Earth music.mp3')

    def mixer(self):
        """
        This function will handle the sounds and when they should be played
        """

    def launching(self):
        if self.launch.get_busy():
            self.countdownlaunchSound.stop()
        self.launch.play(self.countdownlaunchSound)

    def heartBeat(self):
        if self.beat.get_busy():
            self.heartbeepSound.stop()
        self.beat.play(self.heartbeepSound)

    def heartBeatLong(self):
        self.heartbeeplongSound.play()

    def backGroundEarth(self):
        if not self.earthBackground.get_busy():
            self.earthBackground.play(self.earthMusic)


    def backGroundSpace(self):
        pass
