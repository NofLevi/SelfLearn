import pygame, sys
from pygame.locals import *
import game_file
import settings_file
from sprite_sheet_file import sprite_sheet

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
    def start_game(self):
        var = game_file.Game()
        var.start_game()
    
    def settings(self):
        var = settings_file.Settings()
        var.start()
    
    def quit(self):
        self.pygame.quit()
        sys.exit()

    #pygame loop
    def start(self):
        while True:
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()

                    if(x > 110 and x < 290 and y > 120 and y < 180):
                        self.start_game()
                    elif(x > 110 and x < 290 and y > 200 and y < 260):
                        self.settings()
                    elif(x > 110 and x < 290 and y > 280 and y < 360):
                        self.quit()
