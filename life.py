

class Life:

    def __init__(self, genes: dict, birth_time: int):
        self.genes = genes
        self.health = 100.0  # percentage
        self.hunger = 0.0  # percentage
        self.grow_rate = genes['initial_grow_rate']  # how much does organism grow each clock cycle
        self.metabolic_rate = genes['initial_metabolic_rate'] + self.grow_rate  # rate at which hunger is consumed
        self.size = genes['initial_size']  # diameter of organism
        self.birth_time = birth_time  # clock date organism was created
        self.is_dead = False

    def time_update(self) -> None:
        if not self.is_dead:
            self.metabolize()
            self.grow()
            self.heal()
            self.starve()
            if self.health < 0.1:
                self.death()

    def grow(self) -> None:
        if (self.health < 100.0) and (self.hunger < 100.0):
            self.size += self.grow_rate/2
        elif self.hunger < 100.0:
            self.size += self.grow_rate
        else:
            pass

    def heal(self) -> None:
        if (self.health < 100.0) and (self.hunger < 100.0):
            self.health += 1

    def starve(self) -> None:
        if self.hunger > 99.5:
            self.health -= 1

    def metabolize(self) -> None:
        if self.hunger < 99.5:
            self.hunger += self.metabolic_rate

    def death(self) -> None:
        self.genes = {}
        self.health = 0  # percentage
        self.hunger = 0.0  # percentage
        self.grow_rate = 0
        self.metabolic_rate = 0
        self.size = 0
        self.is_dead = True

    def get_is_dead(self) -> bool:
        return self.is_dead

    # it can:
    # 1. grow
    # 2. heal
    # 3. heal and grow
    # 4. loose health when fully hungry
    # 5. not grow or heal when fully hungry
    # 6. metabolize hunger
    # 7. can die

