

class Life:

    def __init__(self, genes: dict, birth_time: int):
        self.genes = genes
        self.health = 100  # percentage
        self.hunger = 100  # percentage
        self.metabolic_rate = genes['initial_metabolic_rate']  # rate at which hunger is converted to other uses
        self.size = genes['initial_size']  # diameter of organism
        self.grow_rate = genes['initial_grow_rate']  # how much does organism grow each clock cycle
        self.birth_time = birth_time  # clock date organism was created

    def time_update(self) -> None:
        self.grow()
        self.heal()

    def grow(self) -> None:
        if self.health < 100:
            self.size += self.grow_rate/2
        else:
            self.size += self.grow_rate

    def heal(self):
        if self.health < 100:
            self.health += 1

