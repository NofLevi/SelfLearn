import pygame
import time
import random

class game():
    def __init__(self, name):  
        self.name = name
        
    #Settings [Default]
    circle_rad = 25
    circle_color = (255,0,0) #Red
    background_color = (0,0,0)
    game_time = 1000
    fps = 240

    #Constants
    WIDTH = 1280
    HEIGHT = 960
    size = (WIDTH,HEIGHT)
    general_center = (WIDTH/2,HEIGHT/2)
    #size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    clock = pygame.time.Clock()

    #Init
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Aim Training") # title
    pygame.draw.circle(screen, circle_color, general_center, circle_rad)#draw first circle to start

    #set font for start the game
    font = pygame.font.SysFont("comicsansms", 72)
    entry_text = font.render("Click on circle to start!!!", True, (0, 128, 0))
    entry_text_rect = entry_text.get_rect(center=(WIDTH/2, HEIGHT/2 - 90))
    screen.blit(entry_text, entry_text_rect)

    #set timer
    timer_text = font.render(str(game_time//100), True, (0, 128, 0))
    timer_text_rect = timer_text.get_rect(center=(WIDTH/2, 30))
    screen.blit(timer_text, timer_text_rect)

    #first update
    pygame.display.update()

    #Game setup
    game_flag = 0
    missed_shots = 0
    target_hits = 0
    center1 = ()
    center2 = ()
    timer = game_time


    def set_timer():
        screen.fill(background_color)
        timer_text = font.render(str(timer//100), True, (0, 128, 0))
        timer_text_rect = timer_text.get_rect(center=(WIDTH/2, 30))
        screen.blit(timer_text, timer_text_rect)
        pygame.draw.circle(screen, circle_color, center1, circle_rad)
        pygame.display.update()
    
    

    #pygame.draw.circle(screen, circle_color, center, circle_rad)

    def random_circle_draw():
        screen.fill(background_color)
        center_W = random.randint(20, size[0]-20)
        center_H = random.randint(70, size[1]-20)
        center = (center_W,center_H)
        pygame.draw.circle(screen, circle_color, center, circle_rad)
        return center

    def finish_game():
        miss_text = font.render(str(timer//100), True, (0, 128, 0))
        miss_text_rect = hit_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(miss_text, miss_text_rect)

        hit_text = font.render(str(timer//100), True, (0, 128, 0))
        hit_text_rect = thit_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 60))
        screen.blit(hit_text, hit_text_rect)
    

    def play():
        
        finish = False
        while not finish:
            if game_flag == 1:
                timer-=1
                if timer%100 == 0:
                    screen.fill(background_color)
                    set_timer()

            if timer <= 0:
                print("Hits: " + str(target_hits) + "\nMiss: " + str(missed_shots))
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
                    if game_flag == 0:
                        if x > general_center[0] - circle_rad and x < general_center[0] + circle_rad and y > general_center[1] - circle_rad and y < general_center[1] + circle_rad:
                            game_flag = 1
                            center1 = random_circle_draw()
                            pygame.display.update()

                    else:
                        if x > center1[0] - circle_rad and x < center1[0] + circle_rad and y > center1[1] - circle_rad and y < center1[1] + circle_rad:
                            target_hits += 1
                            print(target_hits)
                            center1 = random_circle_draw()
                            pygame.display.update()
                        else:
                            missed_shots += 1
            clock.tick(100)
        pygame.quit()


