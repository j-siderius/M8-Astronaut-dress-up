import pygame
import csv
from pygame.locals import *
import time

iniAlive = True
iniDying = False

iniX = 0
situationIndex = 0
nextSection = False

#def heartbeat(sitIn):

class Heartbeat:

	def __init__(self):

		#self.nextSection
		pygame.init()
		pygame.font.init()

		# screen and variables
		self.screen = pygame.display.set_mode((400, 200))
		self.screen_width, screen_height = pygame.display.get_surface().get_size()

		font = pygame.font.SysFont('arial', 18)
		WHITE = (255, 255, 255)
		BLACK = (0, 0, 0)
		GREEN = (100, 255, 0)

		# change BPM here
		self.bpm = 80
		self.ecg = []
		self.scale = 2
		i = 1
		rounds = 0
		self.readHeartrateVolt()
		self.translateRows()

		self.initialY = int(screen_height * 0.5)

		# graphing variables
		self.posX = 0
		self.index = sitIn
		self.situationIndex = sitIn

		# loop variables
		self.running = True
		self.previous_time = 0

	def readHeartrateVolt(self):
		file = open('heart_rate_fullrange.csv')
		csvreader = csv.reader(file)
		self.rows = []
		for row in csvreader:
			self.rows.append(row)
		file.close()

	def translateRows(self):
		for i in range(len(self.rows)):
			rowSpecific = self.rows[i - 1]
			rowText = str(rowSpecific[0])
			rowList = rowText.split('e')
			voltage = float(rowList[0]) * 10 ** (int(rowList[1]))
			self.ecg.append(voltage / 1000 * self.screen_width * self.scale)

	def display(self):
			# clear the screen
			self.screen.fill(BLACK)

			# put string with BPM on screen
			bpm_string = "BPM: " + str(self.bpm)
			bpm_text = font.render(bpm_string, False, WHITE)
			self.screen.blit(bpm_text, (5, 5))

			# increase the x-position every frame
			if self.posX < self.screen_width:
				self.posX += 1
			print(self.posX)
			'''
			else:
				self.posX = 0
				# reset the index if end is reached (loop array)
				index = situationIndex
				print("second option")
				if nextSection == True:
					running = False
					heartbeat(situationIndex+400)
					nextSection = False
			




			# go through all x-positions
			for i in range(posX + 1):
				# calculate the corresponding y-positions
				posY = initialY - int((ecg[index + i] * 100))
				posY2 = initialY - int((ecg[index + i - 1] * 100))

				#print(posY)

				# draw a line between the calculated points
				pygame.draw.line(screen, GREEN, (i, posY), (i-1, posY2), 1)

				# draw a point at the head of the graph
				if i == posX-1:
					pygame.draw.circle(screen, GREEN, (i, posY), 2)

			# update the actual screen
			'''
			pygame.display.update()


beat = Heartbeat()