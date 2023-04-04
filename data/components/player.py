from settings import *
from components.bullet import Bullet
import pygame

class Player():
    gfx_image = pygame.image.load(PLAYER_GFX)
    GFX = pygame.transform.scale(gfx_image, (gfx_image.get_width() * PLAYER_SCALE, gfx_image.get_height() * PLAYER_SCALE))
    bullets = []
    canShoot = True
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        
    # Move the player
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if (self.x > 0):
                self.x -= MOVEMENT_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if (self.x < 600 - self.GFX.get_width()):
                self.x += MOVEMENT_SPEED
            
    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.canShoot == True:
                self.canShoot = False
                left_bullet = Bullet(self.x - 11, self.y - 10)
                right_bullet = Bullet(self.x - 21 + self.GFX.get_width(), self.y - 10)
                self.bullets.append(left_bullet)
                self.bullets.append(right_bullet)
            
    def renderBullets(self, win):
        for bullet in self.bullets:
            bullet.move()
            bullet.render(win)
            if bullet.y < -20:
                self.bullets.remove(bullet)
            
    def render(self, win):
        win.blit(self.GFX, (self.x, self.y))
            
            