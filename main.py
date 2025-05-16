#    main.py

import pygame
from constants import *
from player import Player
from asteroidfield.py import AsteroidField

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    game_clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("Press ESC to exit the game")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)
    
    running = True
    while running:
        for event in pygame.event.get():
            # Both ways to check for QUIT
            if event.type == pygame.QUIT or event.type == 256:  
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill("black")
        for update in updatable:
            update.update(dt)
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

    pygame.quit()
    
if __name__ == "__main__":
    main()
