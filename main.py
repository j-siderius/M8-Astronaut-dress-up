from Screen import Screen
import pygame


def run():
	"""
	Start functions, initializes the screen
	"""
	screen = Screen(0, 0, loop, drawLoop, title="Test window")
	screen.start()


def loop():
	"""
	Main update loop, gets run as often as possible
	"""


def drawLoop():
	"""
	Main draw loop, gets run at fixed interval (determined by framerate)
	"""


if __name__ == '__main__':
	print("Starting program")
	run()
