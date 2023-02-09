import math
import helper_functions

class Life:
    x: float  # in meters
    y: float  # in meters
    heading: float  # in degrees [-180,180]
    speed: float  # m/s
    turning_speed: float  # change in heading


    def __init__(self, x: float, y: float, heading: float, speed: float, turning_speed: float):
        self.x = x
        self.y = y
        self.heading = heading
        self.speed = speed
        self.turning_speed = turning_speed

    def move(self, framerate: float):
        self.heading = helper_functions.degrees_check(self.heading + self.turning_speed)
        self.x += framerate*math.cos(math.radians(self.heading))*self.speed
        self.y += framerate*math.sin(math.radians(self.heading))*self.speed


