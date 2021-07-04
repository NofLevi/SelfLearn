import pygame
import time
import random


#Settings [Default]
circle_rad = 25
circle_color = (255,0,0) #Red
background_color = (0,0,0)

#Constants
WIDTH = 1280
HEIGHT = 960
size = (WIDTH,HEIGHT)
#size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
clock = pygame.time.Clock()

#Init
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Aim Training")
#pygame.draw.circle(screen, circle_color, center, circle_rad)

def random_circle_draw():
    center_W = random.randint(20, size[0]-20)
    center_H = random.randint(20, size[1]-20)
    center = (center_W,center_H)
    pygame.draw.circle(screen, circle_color, center, circle_rad)


finish = False
while not finish:
    for event in pygame.event.get():
        #2 quit options [1.X in corner, 2. escape button]
        if event.type == pygame.QUIT:
            finish = True
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            finish = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if:
                random_circle_draw()
                pygame.display.update()

        
 
pygame.quit()


