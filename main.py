from Screen import Screen
from Sound import Sound
from SerialController import Serial
from DataCalculations import DatCalc
import pygame

# TEST Imports
# TODO: remove and make actual implementation
import random
import time

class Main:

    def __init__(self):
        self.screen = Screen(200, 200, self.loop, self.drawLoop, title="Test window")
        self.sound = Sound()
        self.datCalc = DatCalc()
        self.serial = Serial()
        self.datCalc.dataConnect()

        # TEST Variable
        # TODO: remove
        self.prevTime = 0

    def run(self):
            """
            Start functions, initializes the screen
            """

            self.screen.start()
            self.sound.audioSetup()

            self.serial.serialPorts()

    def loop(self):
        """
		Main update loop, gets run as often as possible
		"""
        
        # TEST Call running every 2 seconds
        # TODO: remove and make actual implementation
        ms = time.time()*1000.0
        if ms > self.prevTime + 2000:
            self.prevTime = ms
            r = random.randint(0, 2)
            if r==0:
                self.serial.writeSerial("A")
            elif r==1:
                var = random.randint(100,999)
                self.serial.writeSerial(("B" + str(var)))
            elif r==2:
                boo = random.randint(0,2)
                self.serial.writeSerial(("C" + str(boo)))
                
    def drawLoop(self):
        """
        Main draw loop, gets run at fixed interval (determined by framerate)
        """

        self.screen.loop()
        self.sound.mixer()


main = Main()

if __name__ == '__main__':
	print("Starting program")
	main.run()

    