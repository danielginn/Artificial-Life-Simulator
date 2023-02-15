

class Life:

    def __init__(self, genes: dict, birth_time: int):
        self.genes = genes
        self.health = 100  # percentage
        self.hunger = 0  # percentage
        self.grow_rate = genes['initial_grow_rate']  # how much does organism grow each clock cycle
        self.metabolic_rate = genes['initial_metabolic_rate'] + self.grow_rate  # rate at which hunger is consumed
        self.size = genes['initial_size']  # diameter of organism
        self.birth_time = birth_time  # clock date organism was created

    def time_update(self) -> None:
        self.grow()
        self.heal()
        self.starve()

    def grow(self) -> None:
        if (self.health < 100) and (self.hunger < 100):
            self.size += self.grow_rate/2
        elif self.hunger < 100:
            self.size += self.grow_rate
        else:
            pass

    def heal(self):
        if (self.health < 100) and (self.hunger < 100):
            self.health += 1

    def starve(self):
        if self.hunger == 100:
            self.health -= 1


    # it can:
    # 1. grow
    # 2. heal
    # 3. heal and grow
    # 4. loose health when fully hungry
    # 5. Not grow or heal when fully hungry

