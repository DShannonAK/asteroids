import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius > ASTEROID_MIN_RADIUS):
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            self.__spawn(new_radius, random_angle)
            self.__spawn(new_radius, -random_angle)
    
    def __spawn(self, radius, angle):
        asteroid = Asteroid(self.position.x, self.position.y, radius)
        vector = self.velocity.rotate(angle)
        asteroid.velocity = vector * 1.2