import pygame
from simucell import SimuCell
import numpy as np
from world import World
import random
import yaml


with open('engine.yml', 'r') as file:
    config = yaml.safe_load(file)
world = World()
pygame.init()

SCREEN_WIDTH = world.width
SCREEN_HEIGHT = world.height
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 163, 0)
RED = (255, 0, 0)
LIGHT_GRAY = (211, 211, 211)
frame_rate = int(config['frame_rate'])

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

num_simucells = int(config['num_simucells'])
simucells = pygame.sprite.Group()
for i in range(num_simucells):
    size = 45
    location = np.array([random.uniform(size//2,world.width-size//2), random.uniform(size//2,world.height-size//2)])
    simucells.add(SimuCell(world, location, random.uniform(-180,180), size, speed=random.uniform(5.0,10.0)))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(LIGHT_GRAY)
    simucells.draw(screen)
    simucells.update()

    pygame.display.update()
    clock.tick(frame_rate)

pygame.quit()
