import pygame
from settings import *

class Meteor():
    gfx_image = pygame.image.load(METEOR_GFX)
    GFX = pygame.transform.scale(gfx_image, (gfx_image.get_width() * METEOR_SCALE, gfx_image.get_height() * METEOR_SCALE))
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        self.y += METEOR_SPEED
        
    def render(self, win):
        win.blit(self.GFX, (self.x, self.y))