from unittest import TestCase
from animal import Animal


class TestAnimal(TestCase):

    def test_class_initialization(self):
        genes = {'initial_size': 2.0, 'initial_metabolic_rate': 0, 'initial_grow_rate': 1.0, 'max_turn_speed': 360, 'max_speed': 100}
        animal = Animal(genes=genes, birth_time=0, x=0, y=0, heading=0)
        self.assertAlmostEqual(animal.health, 100.0, 1)
        self.assertAlmostEqual(animal.speed, 0.0, 1)
        animal.set_speed(2.0)
        self.assertAlmostEqual(animal.speed, 2.0, 1)
        animal.grow()
        self.assertAlmostEqual(animal.size, 3.0, 1)
