"""
This class manages all the other classes in python and will handle the interaction between classes
"""

from Sound import Sound
from SerialController import Serial
from heartBeat import Heartbeat
from DataCalculations import DatCalc
from ErrorMessage import Errormessage
import pygame
import time
import math
import sys


class Main:

    def __init__(self):
        pygame.init()

        # All classes and setups
        self.heartBeatScreen = Heartbeat()
        self.heartBeatScreen.readHeartrateVolt()
        self.heartBeatScreen.translateRows()
        self.sound = Sound()
        self.sound.audioSetup()
        self.datCalc = DatCalc()
        self.datCalc.dataConnect()
        self.serial = Serial(self.datCalc)
        self.error = Errormessage()

        # variables for 60fps loop
        self.frameRate = 60
        self.previous_time = time.perf_counter()
        self.elapsed_time = 0
        self.frameCount = 0

        # variables for flow of program
        self.runBool = False
        self.state = 0
        self.prevState = self.state
        self.planet = "Earth"
        self.prevPlanet = "Earth"
        self.launched = False
        self.preLaunched = False
        self.landed = False
        self.survival = False
        self.errorDisplay = False

        # For def delay
        self.prevTimer = 0
        self.delayBool = True
        self.peakCount = 0

    def run(self):
        """
        Start functions, initializes the screen
        """
        self.runBool = True
        self.serial.encoder("flowState", str(self.state))
        self.loop()

    def loop(self):
        """
        Main update loop, gets run every frame
        """
        while self.runBool:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.K_ESCAPE in self.get_pressed_keys():
                    self.runBool = False
                    sys.exit()

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

        self.planet = self.datCalc.planet

        if self.preLaunched:
            self.errorCheck()

        '''
        #TODO: remove this{
        if self.state == 0:
            if self.delay(100):
                self.state = 1
                self.datCalc.dataRelevant()
        #}
        '''

        # If the user has pressed the big red button
        if self.launched:
            self.launched = False
            self.datCalc.launched = False
            self.state = 1

        # Earth state
        if self.state == 0:
            self.earthState()

        # Launch state
        if self.state == 1:
            self.launchState()

        # Travel state
        if self.state == 2:
            self.travelState()

        # Planet state
        if self.state == 3:
            self.planetState()

        # Death state
        if self.state == 4:
            self.deathState()

        # Survival state
        if self.state == 5:
            self.survivalState()

        if self.prevState != self.state:
            self.prevState = self.state
            self.serial.encoder("flowState", str(self.state))
            self.sound.stopSound()

        # runs every second
        if self.frameCount % 60 == 0:
            print(self.state)
            #pass

    # when the user is still on earth selecting planets
    def earthState(self):
        self.sound.reset()
        self.sound.backGroundEarth()
        if self.prevPlanet != self.planet:
            self.prevPlanet = self.planet
            self.sound.selectPlanet()
            self.datCalc.dataRelevant()
            self.serial.encoder("planetName", self.planet)
            self.serial.encoder("planetData", self.datCalc.curData)
        self.peakCount = 0
        self.preLaunched = self.serial.getLaunched()
        if self.errorDisplay:
            self.error.display()
        elif not self.errorDisplay:
            self.error.displayBlack()

    # when the user pressed the button
    def launchState(self):
        self.serial.setLaunched(False)
        self.sound.launching()
        #travelTime = self.datCalc.getTravelTime()
        if self.delay(1000):
            self.datCalc.survivalCalc()
            self.serial.encoder("travelTime", 10)
            granular = self.datCalc.granular
            print(granular)
            self.serial.encoder("astronautSurvival", granular)

            self.state = 2

    # when the rocket is traveling through space
    def travelState(self):
        self.sound.travel()
        #travelTime = self.datCalc.getTravelTime() * self.frameRate
        if self.delay(600):
            #print(travelTime)
            self.sound.landing()
            self.state = 3

    # when the rocket reached the destination planet
    def planetState(self):
        self.sound.backGroundSpace()
        self.sound.backGroundNoise()
        self.heartBeatScreen.display(self.state)
        survival = self.datCalc.getSurvival()
        data = self.datCalc.getPlanetData()
        granular = self.datCalc.getGranularData()
        if self.delay(200):
            self.landed = True
        if not self.landed:
            if data[3] == "Yes":
                self.sound.oxygen()
        elif self.landed:
            if granular[1] == 1:
                self.sound.oxygen()
        if survival[1]:
            self.survival = True
        else:
            self.survival = False
        if self.landed:
            if self.heartBeatScreen.detectPeak() < 20:
                self.sound.heartBeat()
                self.peakCount += 1
        if not self.survival:
            self.heartBeatScreen.speed *= 1.002
            if self.heartBeatScreen.speed > 4:
                self.state = 4
        elif self.survival:
            self.heartBeatScreen.speed = 1
            if self.peakCount > 10:
                self.state = 5

    # when the astronaut dies
    def deathState(self):
        self.sound.heartBeatLong()
        self.heartBeatScreen.display(self.state)
        self.heartBeatScreen.speed = 0
        if self.delay(400):
            print("Finished")
            self.state = 0
            self.resetValues()

    # when the astronaut survives
    def survivalState(self):
        self.heartBeatScreen.display(self.state)
        self.sound.survived()
        if self.delay(400):
            print("Finished")
            self.state = 0
            self.resetValues()

    # A simple delay check method
    def delay(self, delay):
        if self.delayBool:
            self.delayBool = False
            self.prevTimer = self.frameCount
        if self.prevTimer + delay == self.frameCount:
            self.delayBool = True
            return True

    # Checks for errors when launch happens
    def errorCheck(self):
        error = self.datCalc.returnError()
        if error[0] == 1:
            self.error.setErrorText('You want to stay here?', 'Select a planet to travel to')
            self.errorDisplay = True
            self.serial.setLaunched(False)
        elif error[0] == 2:
            self.error.setErrorText('You can stay at only one planet', 'Select only one planet to travel to')
            self.errorDisplay = True
            self.serial.setLaunched(False)
        elif error[1] == 1:
            self.error.setErrorText('No Aliens Allowed!', 'Check the spacesuit compartment')
            self.errorDisplay = True
            self.serial.setLaunched(False)
        elif error[0] == 0 and error[1] == 0:
            self.error.setErrorText(' ', ' ')
            self.launched = self.preLaunched
            self.preLaunched = False
            self.errorDisplay = False

    def resetValues(self):
        self.state = 0
        self.heartBeatScreen.speed = 1
        self.planet = "Earth"
        self.prevPlanet = "Earth"
        self.launched = False
        self.preLaunched = False
        self.landed = False
        self.survival = False
        self.errorDisplay = False
        self.frameCount = 0
        print("Reset")

    # A test animator, which automatically selects planets and presses launch button
    def testAnimator(self):
        if self.frameCount > 100:
            self.planet = "Jupiter"

        if self.frameCount > 200:
            self.planet = "Mars"

        if self.frameCount == 400:
            self.launched = True

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
