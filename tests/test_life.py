from unittest import TestCase
from life import Life


class TestLife(TestCase):

    def test_should_grow_one_unit_per_turn(self):
        genes = {'initial_size': 2.0, 'initial_metabolic_rate': 0, 'initial_grow_rate': 1.0}
        animal = Life(genes=genes, birth_time=0)
        animal.time_update()
        self.assertAlmostEqual(animal.size, 3.0, 1)

    def test_should_grow_one_unit_in_2_turns(self):
        genes = {'initial_size': 2.0, 'initial_metabolic_rate': 0, 'initial_grow_rate': 0.5}
        animal = Life(genes=genes, birth_time=0)
        animal.time_update()
        animal.time_update()
        self.assertAlmostEqual(animal.size, 3.0, 1)

    def test_should_grow_at_half_rate_when_hurt(self):
        genes = {'initial_size': 2.0, 'initial_metabolic_rate': 0, 'initial_grow_rate': 1.0}
        animal = Life(genes=genes, birth_time=0)
        animal.health = 50
        animal.time_update()
        animal.time_update()
        self.assertAlmostEqual(animal.size, 3.0, 1)

    def test_should_heal_at_1hp_per_turn_when_hurt(self):
        genes = {'initial_size': 2.0, 'initial_metabolic_rate': 0, 'initial_grow_rate': 1.0}
        animal = Life(genes=genes, birth_time=0)
        animal.time_update()
        self.assertEqual(animal.health, 100)
        animal.health = 50
        animal.time_update()
        self.assertEqual(animal.health, 51)

    def test_should_loose_1hp_per_turn_when_fully_hungry(self):
        genes = {'initial_size': 2.0, 'initial_metabolic_rate': 0, 'initial_grow_rate': 1.0}
        animal = Life(genes=genes, birth_time=0)
        animal.hunger = 100
        animal.time_update()
        self.assertEqual(animal.health, 99)

    def test_should_not_grow_or_heal_when_fully_hungry(self):
        genes = {'initial_size': 2.0, 'initial_metabolic_rate': 0, 'initial_grow_rate': 1.0}
        animal = Life(genes=genes, birth_time=0)
        animal.hunger = 100
        animal.health = 50
        animal.time_update()
        self.assertEqual(animal.health, 49)
        self.assertAlmostEqual(animal.size, 2.0, 1)

    def test_living_should_cost_hunger(self):
        genes = {'initial_size': 2.0, 'initial_metabolic_rate': 0.5, 'initial_grow_rate': 0.0}
        animal = Life(genes=genes, birth_time=0)
        animal.time_update()
        self.assertAlmostEqual(animal.hunger, 0.5, 1)

    def test_living_and_growing_should_cost_hunger(self):
        genes = {'initial_size': 2.0, 'initial_metabolic_rate': 0.5, 'initial_grow_rate': 0.5}
        animal = Life(genes=genes, birth_time=0)
        animal.time_update()
        self.assertAlmostEqual(animal.hunger, 1.0, 1)
