from circleshape import *
from constants import *

    # created asteroid class, inherit CircleShape properties
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draw circle
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    # movement in straight line
    def update(self, dt):
        self.position += (self.velocity * dt)

