import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock  = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    Shot.containers = (shots, drawable, updatable)
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for rock in asteroids:
            for shot in shots:
                if rock.collisioncheck(shot):
                    shot.kill()
                    rock.split()
            if rock.collisioncheck(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = game_clock.tick(60)/1000
    
if __name__ == "__main__":
    main()
