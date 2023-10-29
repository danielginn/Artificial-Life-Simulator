import numpy as np
from math import cos, sin, radians, degrees,atan2
import pygame
from world import World


class SimuCell(pygame.sprite.Sprite):
    image: pygame.image
    original_image: pygame.image
    rect: pygame.Rect
    world: World # Reference to the world the SimuCell lives in
    location: np.ndarray # x right, y down
    heading: float # degrees in the clockwise direction from the x-axis
    speed: float # pixels per frame
    size: int

    def __init__(self, world: World, initLocation: np.ndarray, initHeading: float, size: int = 1, speed: float = 0.0):
        super().__init__()
        self.world = world
        self.location = initLocation.copy()
        self.heading = initHeading
        self.original_image = pygame.image.load("bibite.png")
        self.original_image = pygame.transform.scale(self.original_image, (39, 45))
        self.image = self.original_image.copy()
        self.image = pygame.transform.rotate(self.original_image, -self.heading)
        self.rect = self.image.get_rect()
        self.rect.center = (self.location[0],self.location[1])
        self.size = size
        self.speed = speed

    def update(self) -> None:
        velocity = self.speed * np.array([cos(radians(self.heading)), sin(radians(self.heading))])
        self.location += velocity
        boundary_check_code = self.world.boundary_check(self.location, self.size)
        if boundary_check_code > 0:
            self.location -= velocity
            match boundary_check_code:
                case 1:
                    velocity[0] *= -1
                case 2:
                    velocity[1] *= -1
                case 3:
                    velocity *= -1
            self.location += velocity
        self.heading = degrees(atan2(velocity[1], velocity[0]))
        self.rect.center = (self.location[0], self.location[1])
        self.image = pygame.transform.rotate(self.original_image, -self.heading)

    # def get_sprite(self) -> pygame.Rect:
    #     return pygame.Rect(int(self.location[0])-self.size//2, int(self.location[1])-self.size//2, self.size, self.size)
