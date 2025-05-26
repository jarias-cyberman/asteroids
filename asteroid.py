#   asteroid.py

import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def split(self, ):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS   # new asteroid radii
            # Random Angles: plus and minus
            random_angle = random.uniform(20, 50) 
            n_random_angle = random_angle * -1     
            # Direction vectors
            way_one_v = self.velocity.rotate( random_angle + self.velocity.rotate)
            way_two_v = self.velocity.rotate(n_random_angle + self.velocity.rotate)
            
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = way_one_v * 1.2
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = way_two_v * 1.2
        
    def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
""" 
From AsteroidField()
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
"""
