from unittest import TestCase
from living_things import Life


class TestLife(TestCase):

    def setUp(self):
        self.framerate = 1  # fps

    def test_should_move_1_meters_right(self):
        blob = Life(x=0, y=0, orientation=0, speed=1, turning_speed=0)
        blob.move(self.framerate)
        self.assertEqual(blob.x, 1)

    def test_should_move_0_meters_up(self):
        blob = Life(x=0, y=0, orientation=0, speed=1, turning_speed=0)
        blob.move(self.framerate)
        self.assertEqual(blob.y, 0)


