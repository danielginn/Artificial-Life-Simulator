from unittest import TestCase
from living_things import Life


class TestLife(TestCase):

    def setUp(self):
        self.framerate = 1  # fps

    def test_should_move_1_meter_right(self):
        blob = Life(x=0, y=0, orientation=0, speed=1, turning_speed=0)
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 1, 3)
        self.assertAlmostEqual(blob.y, 0, 3)

    def test_should_move_1_meter_up(self):
        blob = Life(x=0, y=0, orientation=90, speed=1, turning_speed=0)
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 0, 3)
        self.assertAlmostEqual(blob.y, 1, 3)

    def test_should_move_1_meter_diagonally_NE(self):
        blob = Life(x=0, y=0, orientation=45, speed=1, turning_speed=0)
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 0.707, 3)
        self.assertAlmostEqual(blob.y, 0.707, 3)

    def test_should_move_2_meters_to_right(self):
        blob = Life(x=0, y=0, orientation=0, speed=2, turning_speed=0)
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 2, 3)
        self.assertAlmostEqual(blob.y, 0, 3)

    def test_should_move_2_meters_diagonally_NE(self):
        blob = Life(x=0, y=0, orientation=45, speed=2, turning_speed=0)
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 1.414, 3)
        self.assertAlmostEqual(blob.y, 1.414, 3)

    def test_should_turn_45_degrees(self):
        blob = Life(x=0, y=0, orientation=0, speed=1, turning_speed=45)
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 0.707, 3)
        self.assertAlmostEqual(blob.y, 0.707, 3)
