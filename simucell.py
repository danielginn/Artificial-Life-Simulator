import numpy as np
from math import cos, sin, radians, degrees,atan2
import pygame
from world import World


class SimuCell:
    world: World # Reference to the world the SimuCell lives in
    location: np.ndarray # x right, y down
    heading: float # degrees in the clockwise direction from the x-axis
    speed: float # pixels per frame
    size: int

    def __init__(self, world: World, initLocation: np.ndarray, initHeading: float, size: int = 1):
        self.world = world
        self.location = initLocation.copy()
        self.heading = initHeading
        self.speed = 0
        self.size = size

    def update_location(self) -> None:
        velocity = self.speed * np.array([cos(radians(self.heading)), sin(radians(self.heading))])
        self.location += velocity
        boundary_check_code = self.world.boundary_check(self.location, self.size)
        if boundary_check_code > 0:
            self.location -= velocity
            old_velocity = velocity.copy()
            match boundary_check_code:
                case 1:
                    velocity[0] *= -1
                case 2:
                    velocity[1] *= -1
                case 3:
                    velocity *= -1
            self.location += velocity
            self.update_heading(velocity)

    def update_heading(self, velocity: np.ndarray) -> None:
        self.heading = degrees(atan2(velocity[1], velocity[0]))


    def get_sprite(self) -> pygame.Rect:
        return pygame.Rect(int(self.location[0])-self.size//2, int(self.location[1])-self.size//2, self.size, self.size)
