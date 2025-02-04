import pygame
from constants import *
from player import *
from asteroid import * 
from asteroidfield import *
import sys

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
    
    # groups to group objects together (cleaner code, Venn diagram like)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player object is added into both created groups
    # Groups can be accessed instead of Player object directly
    # Need to be declared before first instance of Player to catch all instances
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # "places" (calls) player character
    player = Player(x, y)
    asteroidfield = AsteroidField()
    
    # infinite while-loop to keep game running (game-loop)
    while True:
        for event in pygame.event.get(): # calls events to detect quit event
            if event.type == pygame.QUIT:
                return
        
        # fills screen with black color
        pygame.Surface.fill(screen, (0, 0, 0))
        # updates position of all updatables
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if CircleShape.collision_check(bullet, asteroid):
                    pygame.sprite.Sprite.kill(bullet)
                    pygame.sprite.Sprite.kill(asteroid)
    
        for asteroid in asteroids:
            if CircleShape.collision_check(player, asteroid):
               sys.exit("Game Over!")


        # draws all drawables in order
        for character in drawable:
            character.draw(screen)
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