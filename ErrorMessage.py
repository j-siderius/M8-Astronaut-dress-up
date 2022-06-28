# import the pygame module
import pygame
from pygame.locals import *

class Errormessage:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

        self.font = pygame.font.SysFont('arialbold', 50)
        self.font1 = pygame.font.SysFont('arial', 45)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.YELLOW = (230, 230, 0)
        self.text = self.font.render('!', True, self.WHITE)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.screen_width//2, self.screen_height//10 +22)
        self.text1 = self.font1.render('WARNING!', True, self.WHITE)
        self.textRect1 = self.text1.get_rect()
        self.textRect1.center = (self.screen_width//2, self.screen_height//5 +22)
        self.text2 = self.font1.render('No Aliens Allowed', True, self.WHITE)
        self.textRect2 = self.text2.get_rect()
        self.textRect2.center = (self.screen_width//2, self.screen_height//2 -22)
        self.text3 = self.font1.render('Check the spacesuit compartment', True, self.WHITE)
        self.textRect3 = self.text3.get_rect()
        self.textRect3.center = (self.screen_width//2, self.screen_height//2 +22)

    def setErrorText(self, error1, error2):
        self.text2 = self.font1.render(error1, True, self.WHITE)
        self.text3 = self.font1.render(error2, True, self.WHITE)

    def display(self):
        # clear the screen
        self.screen.fill(self.BLACK)

        height = self.screen_height / 14
        pygame.draw.rect(self.screen, self.WHITE, ((self.screen_width/20, height), (self.screen_width/16, height*12)))
        pygame.draw.rect(self.screen, self.WHITE, ((self.screen_width*19/20-self.screen_width/16, height), (self.screen_width/16, height*12)))

        pygame.draw.polygon(self.screen, self.YELLOW, ((self.screen_width / 2 - 30, self.screen_height / 10),
                                                                    (self.screen_width / 2, self.screen_height / 10 + 50),
                                                                    (self.screen_width / 2 + 30, self.screen_height / 10)))
        for x in range(0, 12, 2):
            pygame.draw.polygon(self.screen, self.YELLOW, ((self.screen_width / 20, + height * 2 + height*x),
                                                                (self.screen_width * 9 / 80, + height + height*x),
                                                                (self.screen_width * 9 / 80, + height * 2 + height*x),
                                                                (self.screen_width / 20, + height * 3 + height*x)))
        for x in range(0, 12, 2):
            pygame.draw.polygon(self.screen, self.YELLOW, ((self.screen_width*71/80, + height * 2 + height*x),
                                                                (self.screen_width*19/20, + height + height*x),
                                                                (self.screen_width*19/20, + height * 2 + height*x),
                                                                (self.screen_width*71/80, + height * 3 + height*x)))

        self.screen.blit(self.text, self.textRect)
        self.screen.blit(self.text1, self.textRect1)
        self.screen.blit(self.text2, self.textRect2)
        self.screen.blit(self.text3, self.textRect3)

        pygame.display.update()


errorMessage = Errormessage()


if __name__ == '__main__':
    errorMessage.display()

