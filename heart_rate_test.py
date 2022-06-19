import neurokit2 as nk  # Load the package
import pygame
from pygame.locals import *
import time


def main():
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

	if bpm > 2:
		# ECG min = ±-0.5 max = ±1.5 >> draw 0 at screen_height * 0.75
		ecg = nk.ecg_simulate(duration=16, sampling_rate=100, heart_rate=bpm)
		initialY = int(screen_height * 0.7)
	else:
		# ded
		ecg = [0.0] * screen_width
		initialY = int(screen_height * 0.5)

	# graphing variables
	posX = 0
	index = 0

	# loop variables
	running = True
	previous_time = 0

	while running:
		# handle events
		for event in pygame.event.get():
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
				# increase the index of the array
				if index < len(ecg) - screen_width:
					index += screen_width
				else:
					# reset the index if end is reached (loop array)
					index = 0

			# go through all x-positions
			for i in range(posX):
				# calculate the corresponding y-positions
				posY = initialY - (ecg[index + i] * 100)
				posY2 = initialY - (ecg[index + i - 1] * 100)

				# draw a line between the calculated points
				pygame.draw.line(screen, GREEN, (i, posY), (i-1, posY2), 1)

				# draw a point at the head of the graph
				if i == posX-1:
					pygame.draw.circle(screen, GREEN, (i, posY), 2)

			# update the actual screen
			pygame.display.update()



if __name__ == '__main__':
	main()
