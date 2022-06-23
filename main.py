"""
This class manages all the other classes in python and will handle the interaction between classes
"""

# from Screen import Screen
from Sound import Sound
# from SerialController import Serial
from heartBeat import Heartbeat
from DataCalculations import DatCalc
import pygame
import time


class Main:

    def __init__(self):
        self.heartBeatScreen = Heartbeat
        # self.screen = Screen(200, 200, self.loop, self.drawLoop, title="Test window")
        # self.serial = Serial()
        self.sound = Sound()
        self.sound.audioSetup()
        self.datCalc = DatCalc()
        self.datCalc.dataConnect()
        pygame.init()
        self.frameRate = 60
        self.previous_time = time.perf_counter()
        self.elapsed_time = 0
        self.frameCount = 0
        self.runBool = False

    def run(self):
        """
        Start functions, initializes the screen
        """
        self.runBool = True
        self.loop()

    # self.screen.start()

    # self.serial.serialPorts()

    def loop(self):
        """
        Main update loop, gets run every frame
        """
        while self.runBool:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.K_ESCAPE in self.get_pressed_keys():
                    self.runBool = False

            # timing functions for constant fps
            self.elapsed_time = time.perf_counter() - self.previous_time
            if self.elapsed_time > 1 / self.frameRate:
                self.previous_time = time.perf_counter()
                # draw loop
                self.draw()
                self.frameCount += 1

    def draw(self):
        """
        Put all the functions that need to be called from the main in this method
        """
        self.sound.getFrameCount(self.frameCount)

        self.datCalc.dataRelevant()
        self.datCalc.survivalCalc()

        #print every second
        if self.frameCount % 60 == 0:
            print(self.datCalc.returnSurvival())
            print(self.sound.launching())

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


main = Main()

if __name__ == '__main__':
    main.run()
