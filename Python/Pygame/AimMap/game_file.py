import pygame
import time
import random


class game_class():
    def __init__(self):
        #Settings [Default]
        self.circle_rad = 25
        self.circle_color = (255,0,0) #Red
        self.background_color = (0,0,0)
        self.game_time = 1000
        self.fps = 240

        #Constants
        self.WIDTH = 1280
        self.HEIGHT = 960
        self.size = (self.WIDTH,self.HEIGHT)
        self.general_center = (self.WIDTH/2,self.HEIGHT/2)
        #size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.clock = pygame.time.Clock()

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
        self.center1 = ()
        self.center2 = ()
        self.timer = self.game_time

    def set_timer(self):
        self.screen.fill(self.background_color)
        timer_text = self.font.render(str(self.timer//100), True, (0, 128, 0))
        timer_text_rect = timer_text.get_rect(center=(self.WIDTH/2, 30))
        self.screen.blit(timer_text, timer_text_rect)
        pygame.draw.circle(self.screen, self.circle_color, self.center1, self.circle_rad)
        pygame.display.update()
        
        

    #pygame.draw.circle(screen, circle_color, center, circle_rad)

    def random_circle_draw(self):
        self.screen.fill(self.background_color)
        center_W = random.randint(20, self.size[0]-20)
        center_H = random.randint(70, self.size[1]-20)
        center = (center_W,center_H)
        pygame.draw.circle(self.screen, self.circle_color, center, self.circle_rad)
        return center

    def finish_game(self):
        miss_text = self.font.render(str(self.timer//100), True, (0, 128, 0))
        miss_text_rect = miss_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        self.screen.blit(miss_text, miss_text_rect)

        hit_text = self.font.render(str(self.timer//100), True, (0, 128, 0))
        hit_text_rect = hit_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2 + 60))
        self.screen.blit(hit_text, hit_text_rect)
        
    def start_game(self):    
        finish = False
        while not finish:
            if self.game_flag == 1:
                self.timer-=1
                if self.timer%100 == 0:
                    self.screen.fill(self.background_color)
                    self.set_timer()

            if self.timer <= 0:
                print("Hits: " + str(self.target_hits) + "\nMiss: " + str(self.missed_shots))
                finish = True
                
                
            for event in pygame.event.get():      
                #2 quit options [1.X in corner, 2. escape button]
                if event.type == pygame.QUIT:
                    finish = True
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    finish = True


                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()

                    #first init
                    if self.game_flag == 0:
                        if x > self.general_center[0] - self.circle_rad and x < self.general_center[0] + self.circle_rad and y > self.general_center[1] - self.circle_rad and y < self.general_center[1] + self.circle_rad:
                            self.game_flag = 1
                            self.center1 = self.random_circle_draw()
                            pygame.display.update()

                    else:
                        if x > self.center1[0] - self.circle_rad and x < self.center1[0] + self.circle_rad and y > self.center1[1] - self.circle_rad and y < self.center1[1] + self.circle_rad:
                            self.target_hits += 1
                            print(self.target_hits)
                            self.center1 = self.random_circle_draw()
                            pygame.display.update()
                        else:
                            self.missed_shots += 1
            self.clock.tick(100)
        pygame.quit()
