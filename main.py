#!/usr/bin/env python3

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)


    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)


        #player.draw(screen)
        #player.update(dt)
        pygame.display.flip()
        #clock.tick(60)
        dt = clock.tick(60) / 1000
        



if __name__ == "__main__":
    main()