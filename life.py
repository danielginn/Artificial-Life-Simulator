

class Life:

    def __init__(self, genes: dict, birth_time: int):
        self.genes = genes
        self.health = genes['initial_health']  # percentage
        self.hunger = 100  # percentage
        self.metabolic_rate = genes['initial_metabolic_rate']  # rate at which hunger is converted to other uses
        self.size = genes['initial_size']  # diameter of organism
        self.grow_rate = genes['initial_grow_rate']  # how much does organism grow each clock cycle
        self.birth_time = birth_time  # clock date organism was created

    def time_update(self) -> None:
        self.grow()

    def grow(self) -> None:
        self.size += self.grow_rate
