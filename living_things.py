import math
import helper_functions

class Life:

    def __init__(self, x: float, y: float, heading: float, turning_speed: float, max_turn_speed: float = 360):
        self.x = x  # in meters
        self.y = y  # in meters
        self.heading = heading  # in degrees [-180,180]
        self.speed = 0  # m/s
        self.turning_speed = turning_speed  # change in heading degrees
        self.max_turn_speed = max_turn_speed

    def move(self, framerate: float):
        self.heading = helper_functions.degrees_check(self.heading + self.turning_speed)
        self.x += framerate*math.cos(math.radians(self.heading))*self.speed
        self.y += framerate*math.sin(math.radians(self.heading))*self.speed

    def turn(self, new_turn_speed: float):
        if new_turn_speed > self.max_turn_speed:
            self.turning_speed = self.max_turn_speed
        elif new_turn_speed < -self.max_turn_speed:
            self.turning_speed = -self.max_turn_speed
        else:
            self.turning_speed = new_turn_speed

    def set_speed(self, new_speed:float):
        self.speed = new_speed
