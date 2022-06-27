"""
This class will handle the audio coming from python
"""
import pygame
from pygame import mixer
import time


class Sound:

    def __init__(self):
        """Insert stuff"""

        # For stopping the sounds
        self.currentState = 0

    def audioSetup(self):
        """
        This function will setup the audio
        """

        pygame.mixer.init()
        pygame.mixer.set_num_channels(11)

        # All the mixer channels
        self.buttonPressed = pygame.mixer.Channel(0)
        self.launch = pygame.mixer.Channel(1)
        self.beat = pygame.mixer.Channel(2)
        self.beatLong = pygame.mixer.Channel(3)
        self.earthBackground = pygame.mixer.Channel(4)
        self.planetBackground = pygame.mixer.Channel(5)
        self.noise = pygame.mixer.Channel(6)
        self.select = pygame.mixer.Channel(7)
        self.spaceTravel = pygame.mixer.Channel(8)
        self.enterSpace = pygame.mixer.Channel(9)
        self.victory = pygame.mixer.Channel(10)

        # Individual sounds
        self.selectSound = pygame.mixer.Sound('Sounds/Planet select.wav')
        self.countdownlaunchSound = pygame.mixer.Sound('Sounds/Countdown launch.wav')
        self.buzzerSound = pygame.mixer.Sound('Sounds/Buzzer.wav')
        self.heartbeepSound = pygame.mixer.Sound('Sounds/Heartbeep.wav')
        self.heartbeeplongSound = pygame.mixer.Sound('Sounds/Heartbeep long.wav')
        self.noiseSound = pygame.mixer.Sound('Sounds/Space Noise.wav')
        self.buzLaunchSound = pygame.mixer.Sound('Sounds/Buzlaunch.wav')
        self.doorSound = pygame.mixer.Sound('Sounds/Spaceship Door.wav')
        self.victorySound = pygame.mixer.Sound('Sounds/Victory sound.wav')
        # Background sounds
        self.spaceMusic = pygame.mixer.Sound('Sounds/Space music.mp3')
        self.earthMusic = pygame.mixer.Sound('Sounds/Earth music.mp3')
        self.travelSound = pygame.mixer.Sound('Sounds/TravelSound.wav')

    def selectPlanet(self):
        if self.select.get_busy():
            self.select.stop()
        self.select.play(self.selectSound)

    '''
    def buzzer(self):
        #if not self.buttonPressed.get_busy() and self.buzzerBool:
            self.buttonPressed.play(self.buzzerSound)
            #self.buzzerBool = False
    '''

    def launching(self):
        if not self.launch.get_busy():
            self.launch.play(self.buzLaunchSound)

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
        if not self.planetBackground.get_busy():
            self.planetBackground.play(self.spaceMusic)

    def backGroundNoise(self):
        if not self.noise.get_busy():
            self.noise.play(self.noiseSound)

    def travel(self):
        if not self.spaceTravel.get_busy():
            self.spaceTravel.play(self.travelSound)

    def landing(self):
        self.spaceTravel.fadeout(2)
        if not self.enterSpace.get_busy():
            self.enterSpace.play(self.doorSound)

    def survived(self):
        if not self.victory.get_busy():
            self.victory.play(self.victorySound)

    def stopSound(self):
        """
        Stops all sounds from playing
        """
        self.earthBackground.stop()
        self.planetBackground.stop()
        self.launch.stop()
        self.heartbeepSound.stop()
        self.select.stop()
        self.spaceTravel.stop()
        self.noise.stop()
        self.heartbeeplongSound.stop()

    def reset(self):
        pass
