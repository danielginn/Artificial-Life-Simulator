import pygame
from simucell import SimuCell
import numpy as np
from world import World
import random

pygame.init()
world = World()
SCREEN_WIDTH = world.width
SCREEN_HEIGHT = world.height
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FRAME_RATE = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

num_simucells = 50
simucells = []
for i in range(num_simucells):
    location = np.array([random.uniform(25.0,world.width), random.uniform(25.0,world.height)])
    simucells.append(SimuCell(world, location, random.uniform(-180,180), size=10))
    simucells[i].speed = random.uniform(5.0,15.0)

run = True
while run:
    screen.fill(BLACK)
    for simucell in simucells:
        simucell.update_location()
        pygame.draw.rect(screen, RED, simucell.get_sprite())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FRAME_RATE)

pygame.quit()
