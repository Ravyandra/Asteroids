import pygame
from circleshape import CircleShape
from constants import *

class Lives(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, LIVES_RADIUS)
        self.position.x = x
        self.position.y = y
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

class RocketBar(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, "")
        self.position.x = x
        self.position.y = y
        self.COOLDOWN_BAR = 5
        self.STATUS_FIRE_RATE = False

    def rocket_shot_update(self, CURRENT_COOLDOWN, dt, STATUS):
        self.STATUS_FIRE_RATE = STATUS     
        if self.STATUS_FIRE_RATE == False:
            if CURRENT_COOLDOWN == 5:
                self.COOLDOWN_BAR = 0
            elif 0 < CURRENT_COOLDOWN < 5:
                self.COOLDOWN_BAR += dt 
        elif self.STATUS_FIRE_RATE == True:
            if CURRENT_COOLDOWN >= 5/3:
                self.COOLDOWN_BAR = 0
            elif 0 < CURRENT_COOLDOWN < 5/3:
                self.COOLDOWN_BAR += dt
        
        #self.COOLDOWN_BAR = CURRENT_COOLDOWN

    def rectangle_bar_static(self):
        self.height = 15
        self.width = 50
        return (self.position.x, self.position.y, self.width, self.height)
    
    def rectangle_bar_progress(self):
        if self.STATUS_FIRE_RATE == False:
            self.width_inner = 10 * self.COOLDOWN_BAR
        else:
            self.width_inner = 10 * self.COOLDOWN_BAR * 3
        return (self.position.x, self.position.y, self.width_inner, self.height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.rectangle_bar_static(), 2)
        pygame.Surface.fill(screen, (255, 255, 255), self.rectangle_bar_progress())
    

