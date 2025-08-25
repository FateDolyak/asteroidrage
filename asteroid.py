import pygame, random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            rnd = random.uniform(20,50)
            one = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            two = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            one.velocity = self.velocity.rotate(rnd) * 1.2
            two.velocity = self.velocity.rotate(-rnd) * 1.2
        self.kill()
