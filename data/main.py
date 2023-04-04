import pygame, random, neat, os
from settings import *
import components.player as Player
import components.meteor as Meteor
import components.gui as GUI

pygame.init()  
pygame.font.init()

def game():
    spawn_time = 2000
    pygame.time.set_timer(pygame.USEREVENT + 1, spawn_time)
    win = init_pygame()
    clock = pygame.time.Clock()
    player = Player.Player(300, 650)
    meteors = []
    lifes = 3
    current_bullets = 3
    score = 0
    gui = GUI.GUI(win, clock, lifes)
    
    # Run game loop
    run = True
    while run:
        # Set FPS
        clock.tick(FPS)
        
        # Pygame event handler
        for event in pygame.event.get():
            # If the event is KEYUP and the key was the SpaceBar change the player can shoot boolean to be true
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                player.canShoot = True
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if current_bullets > -1:
                    current_bullets -= 1
                player.current_bullets = current_bullets

            # This event is called each time the pygame timer of USEREVENT is ran
            if event.type == pygame.USEREVENT + 1:
                # Create a new meteor and add it to the meteors list
                new_meteor = Meteor.Meteor(random.randrange(0, WIN_WIDTH - 64), -100)
                meteors.append(new_meteor)
    
                # Change the spawntime if it is over 250
                if spawn_time >= 250:
                    spawn_time -= 25 
                    pygame.time.set_timer(pygame.USEREVENT + 1, spawn_time)
            
            # Basic pygame quit event
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        
        # Set the background of the game
        win.fill((15, 15, 15))
        
        if (lifes <= 0):
            gui.draw_game_over()
        else: 
            # Tick the player
            player.tick(win)
            
            # Tick the meteors
            for meteor in meteors:
                meteor.tick(win)
                
                for bullet in player.bullets:
                    has_collided = meteor.collision(bullet)
                    if (has_collided):
                        player.bullets.remove(bullet)
                        meteors.remove(meteor)
                        score += 1
                        # Add 2 new bullets to current_bullets if the meteor_scale is not the smalest scale
                        current_bullets += (BULLET_ADD * 2 if meteor.meteor_scale == METEOR_MIN_SCALE else BULLET_ADD)
                        
                has_collided = meteor.collision(player)
                
                if (has_collided):
                    meteors.remove(meteor)
                    lifes -= 1
                
                if (meteor.y > WIN_HEIGHT):
                    meteors.remove(meteor)
                    lifes -= 1
          
            gui.tick(lifes, current_bullets, score)
        pygame.display.update()
                
def eval_genomes(genomes, config):
    pass

def init_pygame():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(WINDOW_NAME)
    icon = pygame.image.load(PLAYER_GFX)
    pygame.display.set_icon(icon)
    return win

def train_neat(config_path):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    
    winner = population.run(eval_genomes, 50)
    print('\nBest genome:\n{!s}'.format(winner))

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "../res/neat/config-feedforward.txt")
    
    train_neat(config_path) if USE_NEAT else game()