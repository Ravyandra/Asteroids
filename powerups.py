import pygame
from circleshape import CircleShape
from constants import *
import math

class PowerUp(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_RADIUS)
        self.rotation = 0

    def update(self, dt):
        self.position += (self.velocity * dt)

    def square(self):
        height = (2 * self.radius)/math.sqrt(2)
        width = (2 * self.radius)/math.sqrt(2)
        return (self.position.x, self.position.y, width, height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.square(), 2)

    def effect(self):
        self.kill()