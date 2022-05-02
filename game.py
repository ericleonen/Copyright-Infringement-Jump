import sys
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

playing = True

while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            playing = False

    screen.fill((255, 255, 255))
    pygame.display.flip()