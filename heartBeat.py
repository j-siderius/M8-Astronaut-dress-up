import pygame
import csv
from pygame.locals import *
import time


class Heartbeat:

	def __init__(self):
		pygame.init()
		pygame.font.init()

		# screen and variables
		self.screen = pygame.display.set_mode((400, 200))
		self.screen_width, screen_height = pygame.display.get_surface().get_size()

		self.font = pygame.font.SysFont('arial', 18)
		self.WHITE = (255, 255, 255)
		self.BLACK = (0, 0, 0)
		self.GREEN = (100, 255, 0)

		self.rows = []
		self.ecg = []
		self.scale = 2

		self.initialY = int(screen_height * 0.5)

		# graphing variables
		self.posX = 0
		self.currentFrame = []

		# loop variables
		self.speed = 1
		self.ecgRemember = 0

	def readHeartrateVolt(self):
		file = open('heart_rate_onecycle.csv')
		csvreader = csv.reader(file)
		for row in csvreader:
			self.rows.append(row)
		file.close()

	def translateRows(self):
		for i in range(len(self.rows)):
			rowSpecific = self.rows[i - 1]
			rowText = str(rowSpecific[0])
			rowList = rowText.split('E')
			voltage = float(rowList[0]) * 10 ** (int(rowList[1]))
			self.ecg.append((voltage / (10 ** 21)) * self.screen_width * self.scale)

	def display(self, state):
		# clear the screen
		self.screen.fill(self.BLACK)

		# only run at the appropriate state
		if state == 3 or state == 4:
			# put string with BPM on screen
			bpm_string = "BPM: " + str(int(self.speed * 50))
			bpm_text = self.font.render(bpm_string, False, self.WHITE)
			self.screen.blit(bpm_text, (5, 5))

			ecgPos = int(self.posX * self.speed)

			# increase the x-position every frame
			if self.posX < self.screen_width:
				self.posX += 1
			# if the line leaves the screen, it starts on the lef again
			else:
				self.posX = 0
				self.currentFrame.clear()
				self.ecgRemember = ecgPos % len(self.ecg) + self.ecgRemember

			# fills a list with y-values
			self.currentFrame.append(self.initialY - int((self.ecg[(ecgPos + self.ecgRemember) % len(self.ecg)] * 100)))

			for i in range(len(self.currentFrame)):
				# draw a line between the calculated points
				pygame.draw.line(self.screen, self.GREEN, (i, self.currentFrame[i]), (i - 1, self.currentFrame[i - 1]), 1)

				# draw a point at the head of the graph
				if i == self.posX - 1:
					pygame.draw.circle(self.screen, self.GREEN, (i, self.currentFrame[i]), 2)

		pygame.display.update()

	def detectPeak(self):
		return self.currentFrame[self.posX - 1]

	def changeSpeed(self, speed):
		self.speed = speed