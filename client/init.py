import pygame



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)    
FPS = 120

WINDOWN_WIDTH = 960
WINDOWN_HEIGH = 640
# This sets the WIDTH and HEIGHT of each board location
WIDTH = 28
HEIGHT = 28
# This sets the distance between each cell
MARGIN = 2
rownum = 21
colnum = 21

def get_img(path):
    return pygame.transform.smoothscale(pygame.image.load(path),(28,28))
