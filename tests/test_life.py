from unittest import TestCase
from life import Life


class TestLife(TestCase):

    def test_should_grow_one_unit_per_turn(self):
        genes = {'initial_health': 5, 'initial_size': 2.0, 'initial_metabolic_rate': 0, 'initial_grow_rate': 1.0}
        animal = Life(genes=genes, birth_time=0)
        animal.time_update()
        self.assertAlmostEqual(animal.size, 3.0, 1)

    def test_should_grow_one_unit_in_2_turns(self):
        genes = {'initial_health': 5, 'initial_size': 2.0, 'initial_metabolic_rate': 0, 'initial_grow_rate': 0.5}
        animal = Life(genes=genes, birth_time=0)
        animal.time_update()
        animal.time_update()
        self.assertAlmostEqual(animal.size, 3.0, 1)