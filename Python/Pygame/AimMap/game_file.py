import pygame
import random
import main_menu_file
import winsound
import os
from pygame import mixer
import time

class Game():
    def __init__(self,lst):

        #sound
        sound = mixer.Sound('Sound/mynameisjeff.mp3')
        sound.play()

        #RGB [Colors]
        color_dic = {"Red":(255,0,0),"Black":(0,0,0), "Yellow":(255,255,0),"Purple":(204,0,204),"Blue":(0,0,255),"Green":(0,255,0)}


        #Settings [Default]
        self.circle_rad = 25
        self.circle_color = color_dic[lst[3]]
        self.background_color = color_dic[lst[2]]
        self.game_time = 1000

        
        #Constants
        self.WIDTH = int(lst[0])
        self.HEIGHT = int(lst[1])
        self.size = (self.WIDTH,self.HEIGHT)
        self.general_center = (self.WIDTH/2,self.HEIGHT/2)
        self.clock = pygame.time.Clock()
        os.environ['SDL_VIDEO_CENTERED'] = '1'



        #Init
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Aim Training") # title
        pygame.draw.circle(self.screen, self.circle_color, self.general_center, self.circle_rad)#draw first circle to start

        #set font for start the game
        self.font = pygame.font.SysFont("comicsansms", 72)
        self.entry_text = self.font.render("Click on circle to start!!!", True, (0, 128, 0))
        self.entry_text_rect = self.entry_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2 - 90))
        self.screen.blit(self.entry_text, self.entry_text_rect)

        #set timer
        self.timer_text = self.font.render(str(self.game_time//100), True, (0, 128, 0))
        self.timer_text_rect = self.timer_text.get_rect(center=(self.WIDTH/2, 30))
        self.screen.blit(self.timer_text, self.timer_text_rect)

        #first update
        pygame.display.update()

        #Game setup
        self.game_flag = 0
        self.missed_shots = 0
        self.target_hits = 0
        self.center1 = (self.WIDTH/2,self.HEIGHT/2)
        self.center2 = ()
        self.timer = self.game_time


        #pygame.draw.circle(screen, circle_color, center, circle_rad)




    def random_circle_draw(self):
        self.screen.fill(self.background_color)
        center_W = random.randint(20, self.size[0]-20)
        center_H = random.randint(70, self.size[1]-20)
        center = (center_W,center_H)
        pygame.draw.circle(self.screen, self.circle_color, center, self.circle_rad)
        return center

    def finish_game(self):
        sound = mixer.Sound('Sound/johncena.mp3')
        sound.play()
        self.screen.fill(self.background_color)
        finish_miss_text = self.font.render(str("Hits:" + str(self.target_hits)), True, (0, 128, 0))
        finish_miss_text_rect = finish_miss_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        self.screen.blit(finish_miss_text, finish_miss_text_rect)

        finish_hit_text = self.font.render("Miss:" + str(self.missed_shots), True, (0, 128, 0))
        finish_hit_text_rect = finish_hit_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2 + 60))
        self.screen.blit(finish_hit_text, finish_hit_text_rect)
        pygame.display.update()
        time.sleep(5)
        
    def start_game(self):    
        finish = False
        game_flag = False
        while not finish:
            if(game_flag):
                self.timer -= 1
            
            if self.timer <= 0:
                print("Hits: " + str(self.target_hits) + "\nMiss: " + str(self.missed_shots))
                game_flag = False
                self.finish_game()
                finish = True
            
            if self.timer == self.game_time/2:
                frequency = 1000 
                duration = 100  
                winsound.Beep(frequency, duration)
                winsound.Beep(frequency, duration)
                winsound.Beep(frequency, duration)
                
                
            for event in pygame.event.get():      
                #2 quit options [1.X in corner, 2. escape button]
                if event.type == pygame.QUIT:
                    finish = True
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    finish = True


                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if self.game_flag == False and x > self.general_center[0] - self.circle_rad and x < self.general_center[0] + self.circle_rad and y > self.general_center[1] - self.circle_rad and y < self.general_center[1] + self.circle_rad:
                        game_flag = True
                    #first init
                    if self.game_flag == 0 and game_flag == True:
                        if x > self.general_center[0] - self.circle_rad and x < self.general_center[0] + self.circle_rad and y > self.general_center[1] - self.circle_rad and y < self.general_center[1] + self.circle_rad:
                            self.game_flag = 1
                            self.center1 = self.random_circle_draw()
                            pygame.display.update()

                    elif game_flag == True:
                        if x > self.center1[0] - self.circle_rad and x < self.center1[0] + self.circle_rad and y > self.center1[1] - self.circle_rad and y < self.center1[1] + self.circle_rad:
                            self.target_hits += 1
                            bullet_sound = mixer.Sound('Sound/Gunshot.mp3')
                            bullet_sound.play()
                            print(self.target_hits)
                            self.center1 = self.random_circle_draw()
                            pygame.display.update()
                        else:
                            bullet_sound = mixer.Sound('Sound/nope.mp3')
                            bullet_sound.play()
                            self.missed_shots += 1
            self.clock.tick(100)
        var = main_menu_file.Main_menu()
        var.start()