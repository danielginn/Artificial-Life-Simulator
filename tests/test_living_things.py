from unittest import TestCase
from living_things import Life


class TestLife(TestCase):

    def setUp(self):
        self.framerate = 1  # fps

    def test_should_move_1_meter_right(self):
        blob = Life(x=0, y=0, orientation=0, speed=1, turning_speed=0)
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 1, 4)
        self.assertAlmostEqual(blob.y, 0, 4)

    def test_should_move_1_meter_up(self):
        blob = Life(x=0, y=0, orientation=90, speed=1, turning_speed=0)
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 0, 4)
        self.assertAlmostEqual(blob.y, 1, 4)

    

