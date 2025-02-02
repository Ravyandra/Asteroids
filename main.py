import pygame
from constants import *
from player import *

def main():
    # initiates pygame-module
    pygame.init
    
    # sets screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # calls clock function
    frames_clock = pygame.time.Clock()
    dt = 0 # delta time
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # places player character
    player = Player(x, y)

    # infinite while-loop to keep game running (game-loop)
    while True:
        for event in pygame.event.get(): # calls events to detect quit event
            if event.type == pygame.QUIT:
                return
        
        # fills screen with black color
        pygame.Surface.fill(screen, (0, 0, 0))
        # updates player position
        player.update(dt)
        # draws player
        player.draw(screen)
        # reloads display...
        pygame.display.flip()
        # ...based on 1/60 second ticks (& defines delta time)
        dt = frames_clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

# runs main() only when called through main()
if __name__ == "__main__":
    main()