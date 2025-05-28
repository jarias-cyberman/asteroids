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
            # Random Angles: plus and minus step 2
            cw_random_angle = random.uniform(20, 50) 
            ccw_random_angle = cw_random_angle * -1  
            # Direction vectors step 3
            way_cw_v = pygame.math.Vector2.rotate(self.velocity, cw_random_angle)
            way_ccw_v = pygame.math.Vector2.rotate(self.velocity, ccw_random_angle)
            # new asteroid radii step 4
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # two new asteroid objects
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = way_cw_v * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = way_ccw_v * 1.2

#            AsteroidField.spawn(new_radius, self.position, new_asteroid_1.velocity)
            
#            way_ccw_v = way_ccw_v * 1.2
#            AsteroidField.spawn(new_radius, self.position, new_asteroid_2.velocity)
        
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
