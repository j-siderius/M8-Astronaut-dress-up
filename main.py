"""
This class manages all the other classes in python and will handle the interaction between classes
"""


from Screen import Screen
import pygame


def run():
	"""
	Start functions, initializes the screen
	"""
	screen = Screen(200, 200, loop, drawLoop, title="Test window")
	screen.start()
	sound = Sound()
	sound.audioSetup()
	datCalc = DataCalculations()
	datCalc.dataConnect()
	serial = SerialController()
	serial.serialPorts()



def loop():
	"""
	Main update loop, gets run as often as possible
	"""


def drawLoop():
	"""
	Main draw loop, gets run at fixed interval (determined by framerate)
	"""
	screen.loop()
	sound.mixer()


if __name__ == '__main__':
	print("Starting program")
	run()
