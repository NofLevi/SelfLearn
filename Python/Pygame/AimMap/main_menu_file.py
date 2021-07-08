import pygame, sys
from pygame.locals import *
import game_file

class main_menu_class:
    
    def __init__(self):
        # Setup pygame/window ---------------------------------------- #
        pygame.init()
        pygame.display.set_caption('game base')
        self.screen = pygame.display.set_mode((500, 500),0,32)   
        self.font = pygame.font.SysFont(None, 20)
        self.mainClock = pygame.time.Clock()
        self.click = False
    
    def draw_text(self,text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    def start(self):
        while True:
    
            self.screen.fill((0,0,0))
            self.draw_text('main menu', self.font, (255, 255, 255), self.screen, 20, 20)
    
            mx, my = pygame.mouse.get_pos()
    
            button_1 = pygame.Rect(50, 100, 200, 50)
            button_2 = pygame.Rect(50, 200, 200, 50)
            if button_1.collidepoint((mx, my)):
                if click:
                    self.start_game()
            if button_2.collidepoint((mx, my)):
                if click:
                    self.options()
            pygame.draw.rect(self.screen, (255, 0, 0), button_1)
            pygame.draw.rect(self.screen, (255, 0, 0), button_2)
    
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
    
            pygame.display.update()
            self.mainClock.tick(60)
    
    def start_game(self):
        var = game_file.game_class()
        var.start_game()
    
    def options(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
    
            self.draw_text('options', self.font, (255, 255, 255), self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()
            self.mainClock.tick(60)
    