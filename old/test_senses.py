from unittest import TestCase
from senses import Vision


class TestVision(TestCase):
    def test_Vision_initialization(self):
        vision = Vision(max_range=10, max_fov=20, x=0, y=0, heading=0)
        self.assertAlmostEqual(vision.max_range, 10.0, 1)
        self.assertAlmostEqual(vision.max_fov, 20.0, 1)

    def test_should_find_nearest_of_2_food_pellets(self):
        food_list = [[2, 2], [3, -3]]
        vision = Vision(max_range=10, max_fov=50, x=0, y=0, heading=0)
        self.assertAlmostEqual(vision.find_nearest_food(food_list=food_list), 45.0, 1)
        self.assertEqual(vision.foodVisible, True)
        food_list = [[3, 3], [2, -2]]
        self.assertAlmostEqual(vision.find_nearest_food(food_list=food_list), -45.0, 1)
        self.assertEqual(vision.foodVisible, True)

    def test_should_not_find_food_out_of_sight_range(self):
        food_list = [[20, 20], [30, -30]]
        vision = Vision(max_range=10, max_fov=50, x=0, y=0, heading=0)
        food_angle = vision.find_nearest_food(food_list=food_list)
        self.assertEqual(vision.foodVisible, False)

    def test_should_not_find_food_out_of_sight_fov(self):
        food_list = [[-2, 2], [-3, -3]]
        vision = Vision(max_range=10, max_fov=50, x=0, y=0, heading=0)
        food_angle = vision.find_nearest_food(food_list=food_list)
        self.assertEqual(vision.foodVisible, False)

    def test_should_find_food_when_heading_neg_180(self):
        food_list = [[-2, 2], [-3, -3]]
        vision = Vision(max_range=10, max_fov=50, x=0, y=0, heading=-180)
        self.assertAlmostEqual(vision.find_nearest_food(food_list=food_list), -45.0, 1)
        self.assertEqual(vision.foodVisible, True)

