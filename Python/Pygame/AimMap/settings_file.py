import pygame, sys
from pygame.locals import *
from sprite_sheet_file import sprite_sheet

class Settings:
    # Setup pygame/window ---------------------------------------- #
    pygame.init()
    DISPLAY_W, DISPLAY_H = 600 , 600
    canvas = pygame.Surface((DISPLAY_W,.DISPLAY_H))   
    window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))

    #################################################################
    #setup sprites

    #logo
    canvas.fill((0,0,0))
    my_spritesheet = sprite_sheet('title_settings.png')
    sprite_play = my_spritesheet.get_sprite(0,0,600,100)
    canvas.blit(sprite_play, (0,0))
    window.blit(canvas, (0,0))

    #play button
    my_spritesheet = sprite_sheet('button_apply.png')
    sprite_play = my_spritesheet.get_sprite(0,0,180,60)
    canvas.blit(sprite_play, (5, DISPLAY_H - 55))
    window.blit(canvas, (0,0))
        
    #settings button
    my_spritesheet = sprite_sheet('button_confirm.png')
    sprite_play = my_spritesheet.get_sprite(0,0,180,60)
    canvas.blit(sprite_play, (DISPLAY_W/2 - 90, DISPLAY_H - 55))
    window.blit(canvas, (0,0))
        

    #quitbutton
    my_spritesheet = sprite_sheet('button_cancel.png')
    sprite_play = my_spritesheet.get_sprite(0,0,180,60)
    canvas.blit(sprite_play, (DISPLAY_W - 175, DISPLAY_H - 55))
    window.blit(canvas, (0,0))

    pygame.display.update()
        
    
    #resolution switch
    reso_img_name = ["1920x1080", "1600x900", "1280x720"]
    reso_sprites = dict(((img_name, pygame.image.load(img_name + ".png"))for img_name in self.reso_image_names))
    reso_imp = reso_sprites["1920x1080"]
    #for img_name in car_image_names):
    #    choosen_reso = car_sprites["1920x1080"]
    ##############################################################################

    def car(self, x, y):
        self.window.blit(self.reso_imp, (x, y))
    

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
                    

        pygame.quit()
        exit()