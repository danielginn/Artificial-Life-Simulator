from movement import Movement
from math import atan2, degrees, sqrt
from helper_functions import degrees_check
import sys

class Vision(Movement):
    def __init__(self, max_range: float, max_fov: float, x:float, y:float, heading: float):
        self.max_range = max_range
        self.max_fov = max_fov
        self.x = x
        self.y = y
        self.heading = heading
        self.foodVisible = False

    def find_nearest_food(self, food_list: list[list[float, float]]) -> float:
        nearest_food_distance = sys.float_info.max
        nearest_food_heading = self.heading
        self.foodVisible = False
        for food_item in food_list:
            y_diff = food_item[1] - self.y
            x_diff = food_item[0] - self.x
            angle_food = degrees(atan2(y_diff,x_diff))
            angle_diff = degrees_check(angle_food - self.heading)
            dist = sqrt(x_diff*x_diff + y_diff*y_diff)
            if (abs(angle_diff) < self.max_fov) and (dist < self.max_range) and (dist < nearest_food_distance):
                nearest_food_distance = dist
                nearest_food_heading = angle_diff
                self.foodVisible = True
        return nearest_food_heading



    # Vision functionalities
    # 1. Can find nearby food