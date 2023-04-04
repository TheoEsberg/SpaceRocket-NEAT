import pygame
from settings import *

class GUI():
    
    def __init__(self, win, clock, lifes):
        self.win = win
        self.clock = clock
        self.lifes = lifes
        self.small_font = pygame.font.SysFont(None, SMALL_FONT)
        self.large_font = pygame.font.SysFont(None, LARGE_FONT)
            
    def tick(self, lifes, current_bullets, score):
        self.draw_fps_counter()
        self.draw_lifes(lifes)
        self.draw_bullets(current_bullets)
        self.draw_score(score)
        
    def draw_fps_counter(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.small_font.render("FPS: " + fps, True, (255, 255, 255))
        self.win.blit(fps_text, (WIN_WIDTH - fps_text.get_width() - 10, 10))
        
    def draw_lifes(self, lifes):
        lifes = str(int(lifes))
        lifes_text = self.small_font.render("Lifes: " + lifes, True, (255, 255, 255))
        self.win.blit(lifes_text, (10, 50))
        
    def draw_bullets(self, current_bullets):
        current_bullets = str(int(current_bullets)) if current_bullets >= 0 else str(int(current_bullets + 1))
        current_bullets_text = self.small_font.render("Bullets: " + current_bullets, True, (255, 255, 255))
        self.win.blit(current_bullets_text, (10, 30))
        
    def draw_score(self, score):
        current_score = str(int(score))
        current_score_text = self.small_font.render("Score: " + current_score, True, (255, 255, 255))
        self.win.blit(current_score_text, (10, 10))
        
    def draw_game_over(self):
        game_over_text = self.large_font.render("Game Over!", True, (255, 255, 255))
        self.win.blit(game_over_text, ((WIN_WIDTH / 2) - (game_over_text.get_width() / 2), (WIN_HEIGHT / 2) - (game_over_text.get_height() / 2)))