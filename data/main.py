import pygame, random
from settings import *
import components.player as Player
import components.meteor as Meteor



def main():
    pygame.init() 
    spawn_time = 2000
    pygame.time.set_timer(pygame.USEREVENT + 1, spawn_time)
    win = init_pygame()
    clock = pygame.time.Clock()
    player = Player.Player(300, 650)
    meteors = []
    
    # Run game loop
    run = True
    while run:
        
        # Set FPS
        clock.tick(FPS)
        
        # Pygame event handler
        for event in pygame.event.get():
            
            # If the event is KEYUP and the key was the SpaceBar change the player can shoot boolean to be true
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.canShoot = True

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
            
            has_collided = meteor.collision(player)
            if (has_collided):
                meteors.remove(meteor)
            
            if (meteor.y > WIN_HEIGHT):
                meteors.remove(meteor)
            
            
        pygame.display.update()
                
def init_pygame():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(WINDOW_NAME)
    icon = pygame.image.load(PLAYER_GFX)
    pygame.display.set_icon(icon)
    return win

if __name__ == "__main__":
    main()