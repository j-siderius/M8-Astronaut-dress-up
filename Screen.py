import pygame
from pygame.locals import *
import time


class Screen:
	"""
	Screen class contains functions to process key presses and timing for screen drawing
	"""

	def __init__(self, width: int, height: int, loopfunction, drawfunction, title=None, framerate=60):
		"""
		Initialise the screen
		:param int width: screen width in pixels
		:param int height: screen height in pixels, if no width and height are set, default to full-screen
		:param function loopfunction: action loop
		:param function drawfunction: draw loop
		:param String title: window title
		:param int framerate: frame rate of the screen (also draw loop update frequency)
		"""
		# pygame and screen initialisation
		pygame.init()
		if width == height == 0:
			flags = FULLSCREEN | DOUBLEBUF
			self.screen = pygame.display.set_mode((width, height), flags, 8)
		else:
			self.screen = pygame.display.set_mode((width, height))
		if title:
			pygame.display.set_caption(title)

		# loop variables
		self.frameRate = framerate
		self.previous_time = time.perf_counter()
		self.elapsed_time = 0
		self.loopFunction = loopfunction
		self.drawFunction = drawfunction
		self.run = False

	def loop(self):
		"""
		Main loop of the screen function, call all external functions from here
		- Contains update loop (gets run as often as possible)
		- Contains draw loop (gets run at a specific interval / fps)
		"""
		while self.run:
			# key presses
			for event in pygame.event.get():
				if event.type == pygame.QUIT or pygame.K_ESCAPE in self.get_pressed_keys():
					self.run = False
			# action loop
			self.loopFunction()

			# timing functions for constant fps
			self.elapsed_time = time.perf_counter() - self.previous_time
			if self.elapsed_time > 1 / self.frameRate:
				self.previous_time = time.perf_counter()
				# draw loop
				self.drawFunction()
				# update the screen
				pygame.display.flip()

	def start(self):
		"""
		Starts the main loop
		"""
		self.run = True

	def stop(self):
		"""
		Stops the main loop
		"""
		self.run = False

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
