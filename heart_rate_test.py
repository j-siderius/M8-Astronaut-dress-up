import pygame
import csv
from pygame.locals import *
import time

situationIndex = 0
nextSection = False

def heartbeat(sitIn):
	global nextSection
	pygame.init()
	pygame.font.init()

	# screen and variables
	screen = pygame.display.set_mode((400, 200))
	screen_width, screen_height = pygame.display.get_surface().get_size()

	font = pygame.font.SysFont('arial', 18)
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	GREEN = (100, 255, 0)

	# change BPM here
	bpm = 80
	ecg = []
	scale = 2
	i = 1
	rounds = 0

	file = open('heart_beat_fullrange.csv')

	csvreader = csv.reader(file)
	rows = []
	for row in csvreader:
		rows.append(row)
	file.close()

	for i in range(len(rows)):
		e = rows[i-1]
		d = str(e[0])
		q = d.split('e')
		c = float(q[0]) * 10 ** (int(q[1]))
		ecg.append(c/1000 * screen_width * scale)
		i += 1
		#print(i)

	initialY = int(screen_height * 0.5)

	# graphing variables
	posX = 0
	index = sitIn
	situationIndex = sitIn

	# loop variables
	running = True
	previous_time = 0

	while running:
		# handle events

		for event in pygame.event.get():
			if (event.type == KEYUP):
				print("key pressed")
				nextSection = True
			if event.type == pygame.QUIT:
				running = False

		# update screen at constant framerate (60FPS)
		if time.perf_counter() > previous_time + (1 / 60):
			previous_time = time.perf_counter()

			# clear the screen
			screen.fill(BLACK)

			# put string with BPM on screen
			bpm_string = "BPM: " + str(bpm)
			bpm_text = font.render(bpm_string, False, WHITE)
			screen.blit(bpm_text, (5, 5))

			# increase the x-position every frame
			if posX < screen_width:
				posX += 1
			else:
				posX = 0
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
			pygame.display.update()


if __name__ == '__main__':
	heartbeat(situationIndex)
