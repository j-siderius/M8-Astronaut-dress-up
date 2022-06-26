"""
This class manages all the other classes in python and will handle the interaction between classes
"""

from Sound import Sound
from SerialController import Serial
from heartBeat import Heartbeat
from DataCalculations import DatCalc
import pygame
import time
import math


class Main:

    def __init__(self):
        #self.serial = Serial()
        self.heartBeatScreen = Heartbeat()
        self.heartBeatScreen.readHeartrateVolt()
        self.heartBeatScreen.translateRows()
        self.sound = Sound()
        self.sound.audioSetup()
        self.datCalc = DatCalc()
        self.datCalc.dataConnect()
        pygame.init()
        self.frameRate = 60
        self.previous_time = time.perf_counter()
        self.elapsed_time = 0
        self.frameCount = 0
        self.runBool = False
        self.playDeadOnce = True
        self.state = 0
        self.planet = "Earth"
        self.prevPlanet = "Earth"
        self.launched = False
        self.landed = False
        self.travelDuration = 10

        #For def delay
        self.prevTimer = 0
        self.delayBool = True

    def run(self):
        """
        Start functions, initializes the screen
        """
        self.runBool = True
        self.loop()

    # self.serial.serialPorts()

    def loop(self):
        """
        Main update loop, gets run every frame
        """
        while self.runBool:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.K_ESCAPE in self.get_pressed_keys():
                    self.runBool = False

            # timing functions for constant fps
            self.elapsed_time = time.perf_counter() - self.previous_time
            if self.elapsed_time > 1 / self.frameRate:
                self.previous_time = time.perf_counter()
                # draw loop
                self.draw()
                self.frameCount += 1

    def draw(self):
        """
        Put all the functions that need to be called from the main in this method
        """
        '''
        states:
        Idle
        Travel
        Planet
        Dead
        '''

        #self.serial.readSerial()
        #self.serial.writeSerial()

        self.testAnimator()

        #If the user has pressed the big red button
        if self.launched:
            self.launched = False
            self.state = 1

        #Earth state
        if self.state == 0:
            self.earthState()

        #Launch state
        if self.state == 1:
            self.launchState()

        #Travel state
        if self.state == 2:
            self.travelState()

        #Planet state
        if self.state == 3:
            self.planetState()

        #Death state
        if self.state == 4:
            self.deathState()

        self.sound.stopSound(self.state)

        #runs every second
        if self.frameCount % 60 == 0:
            pass
            #print(self.datCalc.returnSurvival())

    #when the user is still on earth selecting planets
    def earthState(self):
        self.sound.reset()
        self.sound.backGroundEarth()
        if self.prevPlanet != self.planet:
            self.prevPlanet = self.planet
            self.sound.selectPlanet()
            self.datCalc.dataRelevant(self.planet)

    #when the user pressed the button
    def launchState(self):
        self.sound.launching()

        if self.delay(1000):
            self.state = 2

    #when the rocket is traveling through space
    def travelState(self):
        self.sound.travel()
        travelDelay = int((float(self.datCalc.returnDist())**0.25)*self.frameRate*self.travelDuration)
        if self.delay(travelDelay):
            self.sound.landing()
            self.state = 3

    #when the rocket reached the destination planet
    def planetState(self):
        self.sound.backGroundSpace()
        self.sound.backGroundNoise()
        self.heartBeatScreen.display()
        if self.delay(200):
            self.landed = True
        if self.landed:
            if self.heartBeatScreen.detectPeak() < 18:
                self.sound.heartBeat()

    #when the astronaut dies
    def deathState(self):
        self.sound.heartBeatLong()

    def testAnimator(self):
        if self.frameCount > 50:
            self.planet = "Jupiter"

        if self.frameCount > 100:
            self.planet = "Mars"

        if self.frameCount == 200:
            self.launched = True

    # A simple delay check method
    def delay(self, delay):
        if self.delayBool:
            self.delayBool = False
            self.prevTimer = self.frameCount
        if self.prevTimer + delay == self.frameCount:
            self.delayBool = True
            return True

    def get_pressed_keys(self):
        """
        Function processes key presses and adds keys to an array you can check to see if a specific key is pressed
        :returns array of pressed keys
        """
        """
        Keycodes:
        1   30      q   20      a   4       z   29
        2   31      w   26      s   22      x   27
        3   32      e   8       d   7       c   6
        4   33      r   21      f   9       v   25
        5   34      t   23      g   10      b   5
        6   35      y   28      h   11      n   17
        7   36      u   24      j   13      m   16
        8   37      i   12      k   14      ,   54
        9   38      o   18      l   15      .   55
        0   39      p   19      ;   51      /   56
        -   45      +   46      '   52
        """
        pressed_keys = pygame.key.get_pressed()
        active_keys = set(())

        for key_constant, pressed in enumerate(pressed_keys):
            if pressed:
                active_keys.add(key_constant)
        return active_keys


main = Main()

if __name__ == '__main__':
    main.run()
