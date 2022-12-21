import pygame
import pygame_menu
from init import *
from clients import *
from game import *
from home import *

class Menu():
    def __init__(self,screen,client) -> None:
        self.player = client
        self.screen = screen
        
        self.menuTheme = pygame_menu.Theme(
            background_color=pygame_menu.baseimage.BaseImage(image_path="client/image/background.png"),
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
            widget_alignment=pygame_menu.locals.ALIGN_CENTER,
            title=False,
            
        )
        

        self.menu = pygame_menu.Menu(
            height=WINDOWN_HEIGH,
            theme=self.menuTheme,
            title='CARO',
            width=WINDOWN_WIDTH,
            center_content=False,
            mouse_motion_selection=True

        )

        

        self.menu.add.label("Game Caro",
                            font_name=pygame_menu.font.FONT_8BIT,
                            font_size = 70,
                            font_color=(11, 156, 255)
                            ).translate(0, 50)

        self.menu.add.label("(Nhóm 12)",
                            font_name=pygame_menu.font.FONT_OPEN_SANS_ITALIC,
                            font_color=(255, 255, 255),
                            font_size=16,
                            align=pygame_menu.locals.ALIGN_CENTER
                            ).translate(0, 100)

        self.user = self.menu.add.text_input("USERNAME: ",font_name=pygame_menu.font.FONT_OPEN_SANS_ITALIC,
                            font_color=(255, 255, 255),
                            font_size=25,
                            # border_width=1,
                            padding=(0, 50),
                            border_color=(3, 160, 253),
                            maxchar=5,
                            background_color=(0, 14, 51)
                            ).translate(0, 100)

        self.password = self.menu.add.text_input("PASSWORD: ",font_name=pygame_menu.font.FONT_OPEN_SANS_ITALIC,
                            font_color=(255, 255, 255),
                            password=True,
                            align=pygame_menu.locals.ALIGN_CENTER,
                            font_size=25,
                            # border_width=1,
                            padding=(0, 40),
                            border_color=(3, 160, 253),
                            maxchar=8,
                            background_color=(0, 14, 51)
                            ).translate(0, 100)

        self.menu.add.button(' LOG IN', action=self.login,
                             font_color=(51, 191, 251),
                             font_name=pygame_menu.font.FONT_FIRACODE_BOLD,
                             align=pygame_menu.locals.ALIGN_CENTER,
                             border_width=1,
                             font_size=50,
                             padding=(0, 50),
                             cursor=pygame_menu.locals.CURSOR_HAND,
                             border_color=(3, 160, 253),
                             shadow_color=(0, 0, 100),
                             background_color=(0, 14, 51),
                             ).translate(0, 150)
        self.menu.add.button('SIGN IN', self.signin,
                            font_color=(253, 0, 143),
                            font_name=pygame_menu.font.FONT_FIRACODE_BOLD,
                            align=pygame_menu.locals.ALIGN_CENTER,
                            border_width=1,
                            cursor=pygame_menu.locals.CURSOR_HAND,
                            font_size=50,
                            padding=(0, 50),
                            border_color=(3, 160, 253),
                            shadow_color=(0, 0, 100),
                            background_color=(0, 14, 51)
                            ).translate(0, 165)

        # self.menu.add.label("Settings",
        #                     font_name=pygame_menu.font.FONT_8BIT,
        #                     font_color=(255, 255, 255),
        #                     align=pygame_menu.locals.ALIGN_LEFT,
        #                     shadow_color=(0, 0, 100),
        #                     font_size=16
        #                     ).translate(0, 250)
        # self.theme = self.menu.add.toggle_switch('Theme', False, width=100,
        #                     font_name=pygame_menu.font.FONT_NEVIS,
        #                     font_color=(255, 255, 255), padding=0,
        #                     selection_effect=pygame_menu.widgets.NoneSelection(),
        #                     align=pygame_menu.locals.ALIGN_LEFT,
        #                     font_size=16, state_text=('Light', 'Dark'),
        #                     slider_color=(48, 94, 140),
        #                     state_color=((255, 255, 255), (8, 14, 58)),
        #                     switch_margin=(20, 0),
        #                     state_text_font_color=((8, 14, 58), (255, 255, 255)),
        #                     switch_height=1.8,
        #                     switch_border_width=1,
        #                     cursor=pygame_menu.locals.CURSOR_HAND
        #                     ).translate(30, 265)


    def login(self):
        user,passw = self.user.get_value(),self.password.get_value()
        
        if self.player.login(user,passw):
            # print("thanh cong")
            # theme = "dark"
            # if self.theme.get_value():
            #     theme = 'light'
            # game = Game(self.screen,theme).run()
            home = Home(self.screen,user,self.player).run()
        else:
            print('Thatbai')
            self.login

    def signin(self):
        user,passw = self.user.get_value(),self.password.get_value()
        if self.player.singin(user,passw):
            str = "Đăng kí thành công!!!"
        else:
            str = "Đăng kí thất bại!!!!!!!"
        self.menu.add.label(str,
                            font_name=pygame_menu.font.FONT_OPEN_SANS,
                            font_color=(255, 255, 255),
                            font_size=20,
                            align=pygame_menu.locals.ALIGN_CENTER
                            ).translate(0, 250)
        
    def run(self):
        self.menu.mainloop(self.screen)
    
    def loop(self):
        self.menu.mainloop(self.screen,fps_limit=FPS)
