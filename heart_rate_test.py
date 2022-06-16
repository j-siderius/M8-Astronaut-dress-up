import pygame
from pygame.locals import *
from scipy.misc import electrocardiogram
import time


def main():
    # initialize pygame
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((400, 200))
    screen_width, screen_height = pygame.display.get_surface().get_size()

    # grab ECG data from scipy
    ecg = electrocardiogram()  # 360Hz in mV, min: -3.485 max: 3.65
    # screen = 400 x 200
    # 400 points should translate to ±2 seconds
    # 0 mV should be at y 100
    index = 0
    posX = 0  # posX on x-axis

    # initialize font and colours
    font = pygame.font.SysFont('arial', 18)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (100, 255, 0)

    # timing variables
    running = True
    previous_time = previous_beat = time.perf_counter()

    # calculate BPM speed
    bpm_count = int(60)
    _BPM_count = (bpm_count/60) * 200

    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # handle keypresses
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[K_EQUALS]:
                    # if '+' is pressed increase BPM
                    bpm_count += 1
                    _BPM_count = int((bpm_count / 60) * 200)
                elif pygame.key.get_pressed()[K_MINUS]:
                    # if '-' is pressed descrease BPM
                    if bpm_count > 1:
                        bpm_count -= 1
                        _BPM_count = int((bpm_count / 60) * 200)

        # update screen at constant framerate
        if time.perf_counter() > previous_time + (1/30):
            previous_time = time.perf_counter()

            # put string with BPM on screen
            bpm_string = "BPM: " + str(bpm_count)
            bpm_text = font.render(bpm_string, False, WHITE)
            screen.blit(bpm_text, (5, 5))

            # update the actual screen
            pygame.display.update()

        # update ECG at BPM interval
        if time.perf_counter() > previous_beat + (1/_BPM_count):
            previous_beat = time.perf_counter()

            # clear screen
            screen.fill(BLACK)

            # check if we filled the whole screen
            if posX < screen_width:
                # loop through all points up to current cursor position
                for i in range(posX):
                    # get the relevant Y positions
                    posY1 = 100 - (ecg[index + i] * 25)  # center the signal around the middle of the screen
                    posY2 = 100 - (ecg[index + i - 1] * 25)  # previous point
                    # draw a line from previous point to new point
                    pygame.draw.line(screen, GREEN, (i-1, posY2), (i, posY1), 2)

                # calculate the latest point
                leadPosY = 100 - (ecg[index + posX] * 25)
                # draw the leading circle at the leading point
                pygame.draw.circle(screen, GREEN, (posX, leadPosY), 3)
                # increase position on X-axis for next pass
                posX += 1
            else:
                # if position is off screen, reset X-coordinate
                posX = 0
                # check if we reached the end of the ECG data reset if nescessary
                if (index + screen_width) > len(ecg):
                    index = 0
                else:
                    index += screen_width  # pick next set from ECG array


if __name__ == '__main__':
    main()

