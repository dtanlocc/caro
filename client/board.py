import time
import pygame
from init import *
from GameSettings import darktheme
from GameSettings import lighttheme

class Board:
    def __init__(self,screen,theme) -> None:
        
        self.screen = screen
        if theme == 'dark':
            self.color = darktheme.cell
            self.color_board = darktheme.background
        else:
            self.color = lighttheme.cell
            self.color_board = lighttheme.background
        self.grid = []
        for row in range(rownum):
            self.grid.append([])
            for column in range(colnum):
                self.grid[row].append(0)

        self.x_img = get_img("client\image\X_modified-100×100-red.png")
        self.o_img = get_img("client\image\O_modified-100×100-blue.png")
        
    def return_grid(self):
        return self.grid

    def draw_board(self,status):
        self.status = status
        self.screen.fill(self.color_board)
        for row in range(rownum):
            for column in range(colnum):
                
                pygame.draw.rect(self.screen,
                                self.color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
                if self.grid[row][column] == 'x': 
                    self.screen.blit(self.x_img,((WIDTH + MARGIN)*column+2,(HEIGHT + MARGIN)*row+2))
                if self.grid[row][column] == 'o':
                    self.screen.blit(self.o_img,((WIDTH + MARGIN)*column+2,(HEIGHT + MARGIN)*row+2))
        
        if self.status == 3:
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render('Draw', True, GREEN, BLUE)
            textRect = text.get_rect()
            textRect.center = (WINDOWN_WIDTH/2,WINDOWN_HEIGH/2)
            self.screen.blit(text,textRect)
            
        if self.status == 1:
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render('X wins', True, GREEN, BLUE)
            textRect = text.get_rect()
            textRect.center = (WINDOWN_WIDTH/2,WINDOWN_HEIGH/2)
            self.screen.blit(text,textRect)
            # return False
            
        if self.status == 2:
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render('O wins', True, GREEN, BLUE)
            textRect = text.get_rect()
            textRect.center = (WINDOWN_WIDTH/2,WINDOWN_HEIGH/2)
            self.screen.blit(text,textRect)
            # return False

            