import pygame, sys
from pygame.locals import *
import game_file
import settings_file
from sprite_sheet_file import sprite_sheet
from pygame import mixer
class Main_menu:
    
    def __init__(self):
        # Setup pygame/window ---------------------------------------- #
        pygame.init()

        self.DISPLAY_W, self.DISPLAY_H = 400 , 400
        self.canvas = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))   
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))

        #################################################################
        #setup sprites

        #logo
        self.canvas.fill((0,0,0))
        my_spritesheet = sprite_sheet('logo2.jpg')
        self.sprite_play = my_spritesheet.get_sprite(0,0,400,100)
        self.canvas.blit(self.sprite_play, (0,0))
        self.window.blit(self.canvas, (0,0))

        #play button
        my_spritesheet = sprite_sheet('button_play.png')
        self.sprite_play = my_spritesheet.get_sprite(0,0,185,65)
        self.canvas.blit(self.sprite_play, (self.DISPLAY_W/2 - 90, self.DISPLAY_H/2 - 80))
        self.window.blit(self.canvas, (0,0))
        
        #settings button
        my_spritesheet = sprite_sheet('button_settings.png')
        self.sprite_play = my_spritesheet.get_sprite(0,0,180,60)
        self.canvas.blit(self.sprite_play, (self.DISPLAY_W/2 - 90, self.DISPLAY_H/2))
        self.window.blit(self.canvas, (0,0))
        

        #quitbutton
        my_spritesheet = sprite_sheet('button_quit.png')
        self.sprite_play = my_spritesheet.get_sprite(0,0,180,60)
        self.canvas.blit(self.sprite_play, (self.DISPLAY_W/2 - 90, self.DISPLAY_H/2 + 80))
        self.window.blit(self.canvas, (0,0))

        pygame.display.update()
    
    ##########################################################################################
    #class functions

    def start_game(self,lst):
        var = game_file.Game(lst)
        var.start_game()
    
    def settings(self):
        var = settings_file.Settings()
        var.start()
        self.load_config()
    
    def quit(self):
        self.pygame.quit()
        sys.exit()

    def load_config(self):
        with open('config.txt', 'r') as file:
            st = file.readline()
            console_lst = st.split("-")
            reso_lst = console_lst[0].split("x")

            return [reso_lst[0],reso_lst[1],console_lst[1],console_lst[2]]



    #pygame loop
    def start(self):
        while True:
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()

                    if(x > 110 and x < 290 and y > 120 and y < 180):
                        lst = self.load_config()
                        self.start_game(lst)
                    elif(x > 110 and x < 290 and y > 200 and y < 260):
                        self.settings()
                    elif(x > 110 and x < 290 and y > 280 and y < 360):
                        self.quit()
