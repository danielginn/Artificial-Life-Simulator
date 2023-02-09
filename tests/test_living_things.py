from unittest import TestCase
from living_things import Life


class TestLife(TestCase):

    def setUp(self):
        self.framerate = 1  # fps

    def test_should_move_1_meter_right(self):
        blob = Life(x=0, y=0, heading=0, turning_speed=0)
        blob.speed = 1
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 1, 3)
        self.assertAlmostEqual(blob.y, 0, 3)

    def test_should_move_1_meter_up(self):
        blob = Life(x=0, y=0, heading=90, turning_speed=0)
        blob.speed = 1
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 0, 3)
        self.assertAlmostEqual(blob.y, 1, 3)

    def test_should_move_1_meter_diagonally_NE(self):
        blob = Life(x=0, y=0, heading=45, turning_speed=0)
        blob.speed = 1
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 0.707, 3)
        self.assertAlmostEqual(blob.y, 0.707, 3)

    def test_should_move_2_meters_to_right(self):
        blob = Life(x=0, y=0, heading=0, turning_speed=0)
        blob.speed = 2
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 2, 3)
        self.assertAlmostEqual(blob.y, 0, 3)

    def test_should_move_2_meters_diagonally_NE(self):
        blob = Life(x=0, y=0, heading=45, turning_speed=0)
        blob.speed = 2
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 1.414, 3)
        self.assertAlmostEqual(blob.y, 1.414, 3)

    def test_should_turn_45_degrees(self):
        blob = Life(x=0, y=0, heading=0, turning_speed=45)
        blob.speed = 1
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.x, 0.707, 3)
        self.assertAlmostEqual(blob.y, 0.707, 3)
        self.assertAlmostEqual(blob.heading, 45, 1)

    def test_heading_should_be_less_than_positive_180_degrees(self):
        blob = Life(x=0, y=0, heading=170, turning_speed=15)
        blob.speed = 1
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.heading, -175, 1)

    def test_heading_should_be_more_than_negative_180_degrees(self):
        blob = Life(x=0, y=0, heading=-170, turning_speed=-15)
        blob.speed = 1
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.heading, 175, 1)

    def test_heading_should_be_less_than_positive_180_degrees_spun_twice(self):
        blob = Life(x=0, y=0, heading=170, turning_speed=375)
        blob.speed = 1
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.heading, -175, 1)

    def test_heading_should_be_more_than_negative_180_degrees_spun_twice(self):
        blob = Life(x=0, y=0, heading=-170, turning_speed=-375)
        blob.speed = 1
        blob.move(self.framerate)
        self.assertAlmostEqual(blob.heading, 175, 1)

    def test_turning_speed_should_be_set_to_10(self):
        blob = Life(x=0, y=0, heading=0, turning_speed=0)
        blob.speed = 1
        blob.turn(new_turn_speed=10)
        self.assertAlmostEqual(blob.turning_speed, 10, 1)

    def test_turning_speed_should_be_no_more_than_max_turning_speed(self):
        blob = Life(x=0, y=0, heading=0, turning_speed=0, max_turn_speed=10)
        blob.turn(new_turn_speed=50)
        self.assertAlmostEqual(blob.turning_speed, 10, 1)
        blob.turn(new_turn_speed=-50)
        self.assertAlmostEqual(blob.turning_speed, -10, 1)