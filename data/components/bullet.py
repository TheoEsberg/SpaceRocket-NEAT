from settings import *
import pygame

class Bullet():
    gfx_image = pygame.image.load(BULLET_GFX)
    GFX = pygame.transform.scale(gfx_image, (gfx_image.get_width() * BULLET_SCALE, gfx_image.get_height() * BULLET_SCALE))
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # Move bullet
    def move(self):
        self.y -= BULLET_SPEED
        
    # Render the bullet
    def render(self, win):
        win.blit(self.GFX, (self.x, self.y))
        
    # Get the bullet mask
    def get_mask(self):
        return(pygame.mask.from_surface(self.GFX))