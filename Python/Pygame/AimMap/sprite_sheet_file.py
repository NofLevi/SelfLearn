import pygame

class sprite_sheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load("images/" + filename).convert()
    
    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite

    def get_sprite_name(self):
        return self.filename
