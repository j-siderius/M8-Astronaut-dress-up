"""
This class manages all the other classes in python and will handle the interaction between classes
"""

from Screen import Screen
from Sound import Sound
from SerialController import Serial
from DataCalculations import DatCalc
import pygame

class Main:

	def __init__(self):
		self.screen = Screen(200, 200, self.loop, self.drawLoop, title="Test window")
		self.sound = Sound()
		self.datCalc = DatCalc()
		self.serial = Serial()
		self.datCalc.dataConnect()

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
		self.serial.serialPorts()

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
