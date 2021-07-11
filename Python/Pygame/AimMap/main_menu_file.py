import pygame, sys
from pygame.locals import *
import game_file
from sprite_sheet_file import sprite_sheet

class main_menu_class:
    
    def __init__(self):
        # Setup pygame/window ---------------------------------------- #
        pygame.init()
        DISPLAY_W, DISPLAY_H = 800 , 800
        self.canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))   
        self.window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))

        #################################################################
        my_spritesheet = sprite_sheet('button_play.png')
        sprite_play = my_spritesheet.get_sprite(0,0,128,128)
 
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
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

        # loop code
            self.canvas.fill((0,0,0))
            self.canvas.blit(self.sprite_play, (0, self.DISPLAY_H - 128))
            self.window.blit(self.canvas, (0,0))
            pygame.display.update()
            self.mainClock.tick(60)
    
    def start_game(self):
        var = game_file.game_class()
        var.start_game()
    
    def settings(self):
        n = 1
    
    def quit(self):
        self.pygame.quit()
        sys.exit()
