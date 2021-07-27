import pygame
from pygame.locals import *
from sprite_sheet_file import sprite_sheet
import main_menu_file
import os
from pygame import mixer

class Settings:
    # Setup pygame/window ---------------------------------------- #
    def __init__(self):

        sound = mixer.Sound('Sound/wow.mp3')
        sound.play()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.DISPLAY_W, self.DISPLAY_H = 600 , 800
        self.canvas = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)

        #################################################################
        #GUI SETUP


        #logo
        self.canvas.fill((0,0,0))
        self.my_spritesheet = sprite_sheet('title_settings.png')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,600,100)
        self.canvas.blit(self.sprite_play, (0,0))
        self.window.blit(self.canvas, (0,0))

        #apply button
        self.my_spritesheet = sprite_sheet('button_confirm.png')
        self.sprite_play = self.my_spritesheet.get_sprite(0,0,180,60)
        self.canvas.blit(self.sprite_play, (5, self.DISPLAY_H - 125))
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
        self.reso_image_names = [pygame.image.load("images/1600x900.png").convert(), pygame.image.load("images/1280x720.png").convert(), pygame.image.load("images/1024x768.png").convert()]
        self.reso_list = ["1600x900","1280x720", "1024x768"]
        self.reso_imp = self.reso_image_names[0]
        self.window.blit(self.reso_imp, (300, 180))
        self.reso_index = 0

        self.bg_colors_names = [ pygame.image.load("images/Black.png"),  pygame.image.load("images/Red.png"),  pygame.image.load("images/Blue.png"),  pygame.image.load("images/Yellow.png"),  pygame.image.load("images/Green.png"),  pygame.image.load("images/Purple.png")]
        self.bg_list = ["Black","Red","Blue","Yellow","Green","Purple"]
        self.bg_imp = self.bg_colors_names[0]
        self.window.blit(self.bg_imp, (300, 320))
        self.bg_index = 0

        self.circle_colors_names = [ pygame.image.load("images/Black.png"),  pygame.image.load("images/Red.png"),  pygame.image.load("images/Blue.png"),  pygame.image.load("images/Yellow.png"),  pygame.image.load("images/Green.png"),  pygame.image.load("images/Purple.png")]
        self.circle_imp = self.circle_colors_names[1]
        self.window.blit(self.circle_imp, (300, 395))
        self.circle_index = 0

        pygame.display.update()

################################################################
#class funcs

    def update_config(self):
        with open('config.txt', 'w') as file:
            st = self.reso_list[self.reso_index] + "-" + self.bg_list[self.bg_index] + "-" + self.bg_list[self.circle_index]
            file.write(st)

    def resolution_arrow_click(self, side):
        index = 0
        for i in range(3):
            if self.reso_imp == self.reso_image_names[i]:
                index = i

        if index >= 1 and side == "left":
            self.reso_imp = self.reso_image_names[index-1]
            self.window.blit(self.reso_imp, (300, 180))
            self.reso_index = index-1
        
        if index <= 1 and side == "right":
            self.reso_imp = self.reso_image_names[index+1]
            self.window.blit(self.reso_imp, (300, 180))
            self.reso_index = index + 1
    
    def background_arrow_click(self, side):
        index = 0
        for i in range(6):
            if self.bg_imp == self.bg_colors_names[i]:
                index = i
        
        if index >= 1 and side == "left":
            self.bg_imp = self.bg_colors_names[index-1]
            self.window.blit(self.bg_imp, (300, 320))
            self.bg_index = index - 1
        
        if index <= 4 and side == "right":
            self.bg_imp = self.bg_colors_names[index+1]
            self.window.blit(self.bg_imp, (300, 320))
            self.bg_index = index + 1

    
    def circle_arrow_click(self, side):
        index = 0
        for i in range(6):
            if self.circle_imp == self.circle_colors_names[i]:
                index = i
        
        if index >= 1 and side == "left":
            self.circle_imp = self.circle_colors_names[index-1]
            self.window.blit(self.circle_imp, (300, 395))
            self.circle_index = index - 1
        
        if index <= 4 and side == "right":
            self.circle_imp = self.circle_colors_names[index+1]
            self.window.blit(self.circle_imp, (300, 395))
            self.circle_index = index + 1
#
    def position_click_checker(self, x, y):
        if(x > 490 - 50 and x < 490 + 50 and y > 180 - 50 and y < 180 + 50): #resolution right arrow
            self.resolution_arrow_click("right")
            return True 
        elif(x > 235 - 50 and x < 235 + 50 and y > 180 - 50 and y < 180 + 50):#resolution left arrow
            self.resolution_arrow_click("left")
            return True
        elif(x > 490 - 50 and x < 490 + 50 and y > 320 - 50 and y < 320 + 50):#background color right arrow
            self.background_arrow_click("right")
            return True
        elif(x > 235 - 50 and x < 235 + 50 and y > 320 - 50 and y < 320 + 50):#background color left
             self.background_arrow_click("left")
             return True
        elif(x > 490 - 50 and x < 490 + 50 and y > 400 - 50 and y < 400 + 50):#circle color right 
             self.circle_arrow_click("right")
             return True
        elif(x > 235 - 50 and x < 235 + 50 and y > 400 - 50 and y < 400 + 50):#circle color left
             self.circle_arrow_click("left")
             return True
        elif(x > self.DISPLAY_W/2 - 175 - 180 and x < self.DISPLAY_W/2 - 175 +180 and y > self.DISPLAY_H/2 - 125 -60 and y < self.DISPLAY_H/2 - 125 + 60):#cancel button
            return False
        elif(x > 5 - 180 and x < 5 + 180 and y > self.DISPLAY_H - 125 - 60 and y < self.DISPLAY_H - 125 + 60):#confirm button
            self.update_config()

    #pygame loop
    def start(self):
        loop = True
        while loop == True:
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    loop = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        loop = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    loop = self.position_click_checker(x,y)
                    pygame.display.update()

                    

        var = main_menu_file.Main_menu()
        var.start()