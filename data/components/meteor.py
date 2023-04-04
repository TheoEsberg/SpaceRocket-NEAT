import pygame, random
from settings import *

class Meteor():
    gfx_image = pygame.image.load(METEOR_GFX)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.meteor_scale = random.randrange(METEOR_MIN_SCALE, METEOR_MAX_SCALE)
        self.GFX = pygame.transform.scale(self.gfx_image, (self.gfx_image.get_width() * self.meteor_scale, self.gfx_image.get_height() * self.meteor_scale))
        
    # Update the meteor
    def tick(self, win):
        self.move()
        self.render(win)
        print(self.meteor_scale)
        
    # Move the meteor
    def move(self):
        self.y += METEOR_SPEED
        
    # Render the meteor
    def render(self, win):
        win.blit(self.GFX, (self.x, self.y))
        
    # Get the meteor mask
    def get_mask(self):
        return(pygame.mask.from_surface(self.GFX))
        
    # Check for and handle collision
    def collision(self, object):
        object_mask = object.get_mask()
        meteor_mask = self.get_mask()
        offset = (self.x - object.x, self.y - object.y)
        
        # Check for collision
        collision_point = object_mask.overlap(meteor_mask, offset)
        
        # If it has colided with an object return true, else return false
        return bool(collision_point)
        
        
        