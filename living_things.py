from math import sin, cos

class Life:
    x: float  # in meters
    y: float  # in meters
    orientation: float  # in degrees [-180,180]
    speed: float  # m/s
    turning_speed: float  # change in heading


    def __init__(self, x: float, y: float, orientation: float, speed: float, turning_speed: float):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.speed = speed
        self.turning_speed = turning_speed

    def move(self, framerate: float):
        #self.orientation = self.orientation + self.turning_speed
        self.x += framerate*cos(self.orientation)

