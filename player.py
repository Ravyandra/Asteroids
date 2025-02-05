import pygame
from circleshape import CircleShape
from constants import *

# player defined +  inheritance
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = 0
        self.PLAYER_ROCKET_COOLDOWN = 0
        
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
        self.PLAYER_SHOOT_COOLDOWN -= dt
        self.PLAYER_ROCKET_COOLDOWN -= dt
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
            self.shoot_bullet()
        if keys[pygame.K_LCTRL]:
            self.shoot_rocket()
        if keys[pygame.K_ESCAPE]:
            pygame.QUIT()

        #   unit vector 0,0 -> 0,1 + rotation WITH the player       
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot_bullet(self):
        if self.PLAYER_SHOOT_COOLDOWN <= 0:
            self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            Shot(self.position, self.velocity)
            self.PLAYER_SHOOT_COOLDOWN = 0.3

    def shoot_rocket(self):
        if self.PLAYER_ROCKET_COOLDOWN <= 0:
            self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_ROCKET_SPEED
            Rocket(self.position, self.velocity)
            self.PLAYER_ROCKET_COOLDOWN = 5

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


class Rocket(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, ROCKET_RADIUS)
        self.velocity = velocity
    
    # draw circle
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, 2)

    # movement in straight line
    def update(self, dt):
        self.position += (self.velocity * dt)

    def aftershock(self, asteroids):
        self.kill()
        explosion = Rocket(self.position, self.radius)
        explosion.velocity = 0
        explosion.radius *= 9
        for asteroid in asteroids:
            if CircleShape.collision_check(explosion, asteroid):
                asteroid.split()
        explosion.kill()