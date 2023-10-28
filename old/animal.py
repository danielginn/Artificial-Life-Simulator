from life import Life
from movement import Movement

class Animal(Life, Movement):
    def __init__(self, genes: dict, birth_time: int, x: float, y: float, heading: float):
        self.genes = genes
        self.health = 100.0  # percentage
        self.hunger = 0.0  # percentage
        self.grow_rate = genes['initial_grow_rate']  # how much does organism grow each clock cycle
        self.metabolic_rate = genes['initial_metabolic_rate'] + self.grow_rate  # rate at which hunger is consumed
        self.size = genes['initial_size']  # diameter of organism
        self.birth_time = birth_time  # clock date organism was created
        self.age = 0
        self.is_dead = False
        self.x = x  # in meters
        self.y = y  # in meters
        self.heading = heading  # in degrees [-180,180]
        self.speed = 0  # m/s
        self.turning_speed = 0  # change in heading degrees
        self.max_turn_speed = genes['max_turn_speed']
        self.max_speed = genes['max_speed']