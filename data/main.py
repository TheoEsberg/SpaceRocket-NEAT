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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.canShoot = True
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
        
        

        
        win.fill((15, 15, 15))
        player.move()
        player.shoot()
        player.render(win)
        player.renderBullets(win)
        
        for meteor in meteors:
            meteor.move()
            meteor.render(win)
            
        pygame.display.update()
                
def init_pygame():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(WINDOW_NAME)
    icon = pygame.image.load(PLAYER_GFX)
    pygame.display.set_icon(icon)
    return win

if __name__ == "__main__":
    main()