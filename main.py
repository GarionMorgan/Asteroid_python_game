import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #creating screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #pygame time clock to help keep track of time
    clock = pygame.time.Clock()
    dt = 0

    game_loop = True

    while(game_loop):
        #exits out of the game when user quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #background color
        screen.fill((0,0,0))
        #updates the screen
        pygame.display.flip()
        #updates every 60 seconds
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
