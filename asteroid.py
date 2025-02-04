from circleshape import *
from constants import *
import random

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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            asteroid_split_1 = self.velocity.rotate(random_angle)
            asteroid_split_2 = self.velocity.rotate(-random_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, self.radius).velocity = asteroid_split_1 * 1.2
            Asteroid(self.position.x, self.position.y, self.radius).velocity = asteroid_split_2 * 1.2
