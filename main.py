import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #initiate pygame
    pygame.init()
    #creating screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #pygame time clock to help keep track of time
    clock = pygame.time.Clock()

    #adding groups to help reduce CPU usage and keep track of objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #container for asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    #initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    dt = 0

    game_loop = True

    while(game_loop):
        #exits out of the game when user quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #updates the player
        updatable.update(dt)
        #background color
        screen.fill((0,0,0))
        #draw the player
        for obj in drawable:
            obj.draw(screen)

        #updates the screen
        pygame.display.flip()
        #limit the framework to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
