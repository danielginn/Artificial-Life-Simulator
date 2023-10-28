import numpy as np
from math import cos, sin, radians


class SimuCell:
    location: np.ndarray # x right, y down
    heading: float # degrees in the clockwise direction from the x-axis
    speed: float # pixels per frame

    def __init__(self, initLocation: np.ndarray, initHeading: float):
        self.location = initLocation.copy()
        self.heading = initHeading
        self.speed = 0

    def updateLocation(self):
        velocity = self.speed * np.array([cos(radians(self.heading)), sin(radians(self.heading))])
        self.location += velocity
