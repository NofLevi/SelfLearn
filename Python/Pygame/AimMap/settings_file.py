import pygame, sys
from pygame.locals import *
from sprite_sheet_file import sprite_sheet
import dropdown_class_file

class settings_class:
    
    def __init__(self):
        # Setup pygame/window ---------------------------------------- #
        pygame.init()
        self.DISPLAY_W, self.DISPLAY_H = 600 , 600
        self.canvas = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))   
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))

        #################################################################
        #setup sprites

        #logo
        self.canvas.fill((0,0,0))
        my_spritesheet = sprite_sheet('title_settings.png')
        self.sprite_play = my_spritesheet.get_sprite(0,0,600,100)
        self.canvas.blit(self.sprite_play, (0,0))
        self.window.blit(self.canvas, (0,0))

        #play button
        my_spritesheet = sprite_sheet('button_apply.png')
        self.sprite_play = my_spritesheet.get_sprite(0,0,180,60)
        self.canvas.blit(self.sprite_play, (5, self.DISPLAY_H - 55))
        self.window.blit(self.canvas, (0,0))
        
        #settings button
        my_spritesheet = sprite_sheet('button_confirm.png')
        self.sprite_play = my_spritesheet.get_sprite(0,0,180,60)
        self.canvas.blit(self.sprite_play, (self.DISPLAY_W/2 - 90, self.DISPLAY_H - 55))
        self.window.blit(self.canvas, (0,0))
        

        #quitbutton
        my_spritesheet = sprite_sheet('button_cancel.png')
        self.sprite_play = my_spritesheet.get_sprite(0,0,180,60)
        self.canvas.blit(self.sprite_play, (self.DISPLAY_W - 175, self.DISPLAY_H - 55))
        self.window.blit(self.canvas, (0,0))

        pygame.display.update()

##############################################################################
#drop down setup
        COLOR_INACTIVE = (100, 80, 255)
        COLOR_ACTIVE = (100, 200, 255)
        COLOR_LIST_INACTIVE = (255, 100, 100)
        COLOR_LIST_ACTIVE = (255, 150, 150)
        self.list1 = dropdown_class_file.DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    50, 50, 200, 50, 
    pygame.font.SysFont(None, 30), 
    "Select Mode", ["Calibration", "Test"])
    

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
                    
                
                selected_option = self.list1.update(event)
                if selected_option >= 0:
                    print(selected_option)


                self.screen.fill((255, 255, 255))
                self.list1.draw(self.screen)
                pygame.display.flip()

        pygame.quit()
        exit()