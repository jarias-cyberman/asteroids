#   asteroid.py

import pygame
from constants import *
from player import Player

Asteroid.containers = (asteroids, updatable, drawable)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super() __init__(self, x, y, radius):
        
    def draw(self, screen):
         pygame.draw.circle(screen, "White", position, radius, 2)

    def update(self, dt)
        self.position += self.velocity * dt

    
