import pygame, sys
from pygame.locals import *
from sprite_sheet_file import sprite_sheet

class Settings:
    # Setup pygame/window ---------------------------------------- #
    def __init__(self):
        pygame.init()
        self.DISPLAY_W, self.DISPLAY_H = 600 , 800
        self.canvas = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)

        #################################################################
        #setup sprites

        #logo
        self.canvas.fill((0,0,0))
        self.my_spritesheet = sprite_sheet('title_settings.png')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,600,100)
        self.canvas.blit(self.sprite_play, (0,0))
        self.window.blit(self.canvas, (0,0))

        #apply button
        self.my_spritesheet = sprite_sheet('button_apply.png')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,180,60)
        self.canvas.blit(self.sprite_play, (5, self.DISPLAY_H - 125))
        self.window.blit(self.canvas, (0,0))
            
        #confirm button
        self.my_spritesheet = sprite_sheet('button_confirm.png')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,180,60)
        self.canvas.blit(self.sprite_play, (self.DISPLAY_W/2 - 90, self.DISPLAY_H - 125))
        self.window.blit(self.canvas, (0,0))
            

        #cancel button
        self.my_spritesheet = sprite_sheet('button_cancel.png')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,180,60)
        self.canvas.blit(self.sprite_play, (self.DISPLAY_W - 175, self.DISPLAY_H - 125))
        self.window.blit(self.canvas, (0,0))

        #settings right arrows
        self.my_spritesheet = sprite_sheet('button_arrow_right.bmp')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,50,50)
        self.canvas.blit(self.sprite_play, (490, 180))
        self.window.blit(self.canvas, (0,0))

        self.my_spritesheet = sprite_sheet('button_arrow_right.bmp')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,50,50)
        self.canvas.blit(self.sprite_play, (490, 320))
        self.window.blit(self.canvas, (0,0))

        self.my_spritesheet = sprite_sheet('button_arrow_right.bmp')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,50,50)
        self.canvas.blit(self.sprite_play, (490, 400))
        self.window.blit(self.canvas, (0,0))

        #settings left arrows
        self.my_spritesheet = sprite_sheet('button_arrow_left.bmp')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,50,50)
        self.canvas.blit(self.sprite_play, (235, 180))
        self.window.blit(self.canvas, (0,0))

        self.my_spritesheet = sprite_sheet('button_arrow_left.bmp')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,50,50)
        self.canvas.blit(self.sprite_play, (235, 320))
        self.window.blit(self.canvas, (0,0))

        self.my_spritesheet = sprite_sheet('button_arrow_left.bmp')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,50,50)
        self.canvas.blit(self.sprite_play, (235, 400))
        self.window.blit(self.canvas, (0,0))



        #settings text
        self.font = pygame.font.SysFont("comicsansms", 40)
        self.entry_text = self.font.render("Video:", True, (255, 0, 0))
        self.entry_text_rect = self.entry_text.get_rect(center=(90, 140))
        self.window.blit(self.entry_text, self.entry_text_rect)
        
        self.font = pygame.font.SysFont("comicsansms", 32)
        self.entry_text = self.font.render("Resolution:", True, (0, 128, 0))
        self.entry_text_rect = self.entry_text.get_rect(center=(90, 200))
        self.window.blit(self.entry_text, self.entry_text_rect)

        self.font = pygame.font.SysFont("comicsansms", 40)
        self.entry_text = self.font.render("Colors:", True, (255, 0, 0))
        self.entry_text_rect = self.entry_text.get_rect(center=(90, 280))
        self.window.blit(self.entry_text, self.entry_text_rect)

        self.font = pygame.font.SysFont("comicsansms", 32)
        self.entry_text = self.font.render("Background:", True, (0, 128, 0))
        self.entry_text_rect = self.entry_text.get_rect(center=(90, 340))
        self.window.blit(self.entry_text, self.entry_text_rect)

        self.font = pygame.font.SysFont("comicsansms", 32)
        self.entry_text = self.font.render("Circles:", True, (0, 128, 0))
        self.entry_text_rect = self.entry_text.get_rect(center=(90, 420))
        self.window.blit(self.entry_text, self.entry_text_rect)

        self.font = pygame.font.SysFont("comicsansms", 40)
        self.entry_text = self.font.render("Sound:", True, (255, 0, 0))
        self.entry_text_rect = self.entry_text.get_rect(center=(90, 510))
        self.window.blit(self.entry_text, self.entry_text_rect)

        self.font = pygame.font.SysFont("comicsansms", 32)
        self.entry_text = self.font.render("Hits/Miss:", True, (0, 128, 0))
        self.entry_text_rect = self.entry_text.get_rect(center=(90, 575))
        self.window.blit(self.entry_text, self.entry_text_rect)

        self.font = pygame.font.SysFont("comicsansms", 32)
        self.entry_text = self.font.render("Half Time", True, (0, 128, 0))
        self.entry_text_rect = self.entry_text.get_rect(center=(90, 635))
        self.window.blit(self.entry_text, self.entry_text_rect)

 
        # switch
        self.reso_image_names = ["1920x1080", "1600x900", "1280x720"]
        self.reso_sprites = dict(((img_name, pygame.image.load(img_name + ".png"))for img_name in self.reso_image_names))
        self.reso_imp = self.reso_sprites["1920x1080"]
        self.window.blit(self.reso_imp, (300, 180))

        self.reso_image_names = ["Black", "Red", "Blue", "Yellow", "Green", "Purple"]
        self.reso_sprites = dict(((img_name, pygame.image.load(img_name + ".png"))for img_name in self.reso_image_names))
        self.reso_imp = self.reso_sprites["Black"]
        self.window.blit(self.reso_imp, (300, 320))

        self.reso_image_names = ["Black", "Red", "Blue", "Yellow", "Green", "Purple"]
        self.reso_sprites = dict(((img_name, pygame.image.load(img_name + ".png"))for img_name in self.reso_image_names))
        self.reso_imp = self.reso_sprites["Red"]
        self.window.blit(self.reso_imp, (300, 395))

#r


        pygame.display.update()

################################################################
#class funcs
    def position_click_checker(self, x, y):
        if(x > 490 - 50 and x < 490 + 50 and y > 180 - 50 and y < 180 + 50): #resolution right arrow
            x = 5
        elif(x > 235 - 50 and x < 235 + 50 and y > 180 - 50 and y < 180 + 50):#resolution left arrow
            y = 5
        elif(x > 490 - 50 and x < 490 + 50 and y > 320 - 50 and y < 320 + 50):#background color right arrow
            x = 5
        elif(x > 235 - 50 and x < 235 + 50 and y > 320 - 50 and y < 320 + 50):#background color left
            y = 5
        elif(x > 490 - 50 and x < 490 + 50 and y > 400 - 50 and y < 400 + 50):#circle color right 
            x = 5
        elif(x > 235 - 50 and x < 235 + 50 and y > 400 - 50 and y < 400 + 50):#circle color left
            y = 5
        elif(x > self.DISPLAY_W/2 - 90 -180 and x < self.DISPLAY_W/2 - 90 + 180 and y > self.DISPLAY_H - 125 - 60 and y < self.DISPLAY_H - 125 + 60):#confirm button
            x = 5
        elif(x > self.DISPLAY_W - 175 - 180 and x < self.DISPLAY_W - 175 +180 and y > self.DISPLAY_H - 125 -60 and y < self.DISPLAY_H - 125 + 60):#cancel button
            x = 5
        elif(x > 5 - 180 and x < 5 + 180 and y > self.DISPLAY_H - 125 - 60 and y < self.DISPLAY_H - 125 + 60):#apply button
            x = 5

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
                    self.position_click_checker(x,y)

                    

        pygame.quit()
        exit()