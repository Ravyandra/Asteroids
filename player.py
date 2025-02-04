import pygame
from circleshape import CircleShape
from constants import *

# player defined +  inheritance
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
        # function to set triangle geometry
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

        # draw player (called in main())
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

        # rotation formula
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

        # update player position
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # A key
            self.rotate(-dt)
        if keys[pygame.K_d]: # D key
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        #   unit vector 0,0 -> 0,1 + rotation WITH the player       
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        Shot(self.position, self.velocity)

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
    # draw circle
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, 2)

    # movement in straight line
    def update(self, dt):
        self.position += (self.velocity * dt)