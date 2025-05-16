"""
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        # Fill the screen with black
        screen.fill("black")  # or (0, 0, 0)
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()


# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event detected!")
                return
        screen.fill("black")  #  (0,0,0)
        pygame.display.flip()
    
if __name__ == "__main__":
    main()


import pygame
import sys
from constants import *
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event detected!")
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape key pressed!")
                    running = False
        
        screen.fill("black")
        pygame.display.flip()
    
    print("Game loop ended, closing pygame...")
    pygame.quit()
    print("Pygame closed, exiting program...")
    
if __name__ == "__main__":
    main()
    
    
import pygame
import sys
from constants import *
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")  # Setting a window title

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        # Process all events at the start of each frame
        for event in pygame.event.get():
            print(f"Event detected: {event.type}")  # This will print every event type
            if event.type == pygame.QUIT:
                print("Quit event detected!")
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape key pressed!")
                    running = False
        
        screen.fill("black")
        pygame.display.flip()
    
    print("Game loop ended")
    pygame.quit()
    
if __name__ == "__main__":
    main()
"""
