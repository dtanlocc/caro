from menu import *
from init import *
import pygame
from clients import *



def run():
    pygame.init()
    screen = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGH))
    pygame.display.set_caption('Trò chơi cờ caro')
    main = Menu(screen,Client())
    main.run()

if __name__ == "__main__":
    run()
    