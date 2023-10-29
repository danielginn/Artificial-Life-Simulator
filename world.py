import numpy as np
import yaml

class World():
    width: int
    height: int

    def __init__(self, filepath):
        try:
            with open(filepath, 'r') as file:
                world = yaml.safe_load(file)
            self.width = int(world['width'])
            self.height = int(world['height'])
            file.close()
        except FileNotFoundError:
            msg = "Sorry, the {} file does not exist.".format(filepath)
            print(msg)
    def boundary_check(self, location: np.ndarray, size: int) -> int:
        result = 0
        if (int(location[0])-size//2 < 0) or (int(location[0])+size//2 > self.width):
            result += 1
        if (int(location[1])-size//2 < 0) or (int(location[1])+size//2 > self.height):
            result += 2
        return result

