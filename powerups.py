import pygame
from circleshape import CircleShape
from constants import *

class PowerUp(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_RADIUS)
        self.rotation = 0

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rotation += 1

    def square(self):
        side = pygame.Vector2(0,1).rotate(self.rotation) * self.radius
        side_rotated = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius
        upper_left = self.position + side - side_rotated
        upper_right = self.position + side + side_rotated
        lower_left = self.position - side - side_rotated
        lower_right = self.position - side + side_rotated
        return [upper_left, upper_right, lower_left, lower_right]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.square(), 2)

    