from menu import *
from init import *
import pygame

pygame.init()
screen = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGH))
pygame.display.set_caption('Trò chơi cờ caro')

if __name__ == "__main__":
    main = Menu(screen)
    main.run()