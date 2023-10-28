import pygame
from simucell import SimuCell
import numpy as np
from world import World

pygame.init()
world = World()
SCREEN_WIDTH = world.width
SCREEN_HEIGHT = world.height
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FRAME_RATE = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

simucell = SimuCell(world, np.array([25.0, 300.0]), 0.0, size=50)
simucell.speed = 10

run = True
while run:
    screen.fill(BLACK)
    simucell.update_location()
    pygame.draw.rect(screen, RED, simucell.get_sprite())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FRAME_RATE)

pygame.quit()
