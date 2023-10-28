import numpy as np
from math import cos, sin, radians
import pygame


class SimuCell:
    location: np.ndarray # x right, y down
    heading: float # degrees in the clockwise direction from the x-axis
    speed: float # pixels per frame
    size: int

    def __init__(self, initLocation: np.ndarray, initHeading: float, size: int = 1):
        self.location = initLocation.copy()
        self.heading = initHeading
        self.speed = 0
        self.size = size

    def update_location(self) -> None:
        velocity = self.speed * np.array([cos(radians(self.heading)), sin(radians(self.heading))])
        self.location += velocity

    def get_sprite(self) -> pygame.Rect:
        return pygame.Rect(int(self.location[0]), int(self.location[1]), self.size, self.size)
