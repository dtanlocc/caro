import pygame
import pygame_menu
from init import *
from board import *


class Game:
    def __init__(self,screen,theme="white") -> None:
        self.XO = XO
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.x_img = get_img("image\X_modified-100×100-red.png")
        self.o_img = get_img("image\O_modified-100×100-blue.png")
        self.board = Board(self.screen,theme)
        self.grid = self.board.return_grid()

    

    

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // (WIDTH + MARGIN)
                    row=  pos[1] // (HEIGHT + MARGIN)
                    if self.grid[row][col] == 0:
                        if self.XO == 'x':
                            self.grid[row][col] = self.XO
                            self.XO = 'o'
                        else:
                            self.grid[row][col] = self.XO
                            self.XO = 'x'
            
            

            self.board.draw_board()
            self.clock.tick(FPS)
            pygame.display.update()

