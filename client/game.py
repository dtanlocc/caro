import pygame
import pygame_menu
from init import *
from board import *


class Game:
    def __init__(self,screen,roomid,client,check,X0,theme="light") -> None:
        self.client = client
        self.roomid = roomid
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.x_img = get_img("image\X_modified-100×100-red.png")
        self.o_img = get_img("image\O_modified-100×100-blue.png")
        self.board = Board(self.screen,theme)
        self.grid = self.board.return_grid()
        self.X0 = X0
        self.status = None
        self.check = self.client.ready_room(self.roomid)
    
    def move_player2(self):
        try:
            self.client.move(self.roomid,"0",0,0)
            a,b,c=self.client.recv_move()
            self.grid[int(b)][int(c)] = a
            self.status = int(self.client.win(self.roomid))
            self.board.draw_board(status=self.status)
            pygame.display.update()
            # return True
        except:
            print("Not bad")
            # return False

    def run(self):
        
        # if self.X0 == "x":
        #     while True:
        #         try:
        #             self.start = self.client.start()
        #             break
        #         except:
        #             print("Dang doi doi thu!")
        running = True

        self.board.draw_board(self.status)
        pygame.display.update()
        # while True:
        if self.X0 == "o":
            self.move_player2()
                # self.start = True
                # break
            # else:
            #     self.start = self.client.start(self.roomid)
            #     if self.start:
            #         print("tim thay doi thu")
            #         time.sleep(10)
            #         break
            #     else:
            #         print("Chua tim thay doi thu")
        self.check = False
        while running:
            # self.move_player2()
            # self.status = int(self.client.win(self.roomid))
            # self.board.draw_board(self.status)
            # pygame.display.update()
            # if self.status != 0:
            #     time.sleep(5)
            #     running = False
            
            
            for event in pygame.event.get():
                
                # if self.client.leave_room(self.roomid):
                if event.type == pygame.QUIT:
                    if self.X0 =="x":
                        self.client.leave_room(self.roomid,2)
                        self.board.draw_board(2)
                        pygame.display.update()
                        time.sleep(5)
                    else:
                        self.client.leave_room(self.roomid,1)
                        self.board.draw_board(1)
                        pygame.display.update()
                        time.sleep(5)
                    running = False
                # if self.start:
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // (WIDTH + MARGIN)
                    row=  pos[1] // (HEIGHT + MARGIN)
                    try:
                        
                        if self.grid[row][col] == 0 or self.grid[row][col] == "0":
                            if self.X0 == 'x':
                                self.grid[row][col] = self.X0
                            else:
                                self.grid[row][col] = self.X0
                        self.board.draw_board(self.status)
                        pygame.display.update()
                        self.client.move(self.roomid,self.X0,row,col)
                        if self.client.leave_room(self.roomid,self.status):
                            self.check = True
                        a,b,c=self.client.recv_move()
                        self.grid[int(b)][int(c)] = a
                        self.status = int(self.client.win(self.roomid))
                        self.board.draw_board(self.status)
                        pygame.display.update()
                        
                    except:
                        pass
                
            
            # print(self.grid)
            
            
            
            

            if (self.status == 1 or self.status == 2) and self.check:
                # self.client.leave_room(self.roomid)
                time.sleep(5)
                running = False

            self.clock.tick(FPS)
            pygame.display.update()
        # time.sleep(1000)

    

