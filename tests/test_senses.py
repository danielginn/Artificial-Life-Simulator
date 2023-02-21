from unittest import TestCase
from senses import Vision


class TestVision(TestCase):
    def test_Vision_initialization(self):
        vision = Vision(max_range=10, max_fov=20)
        self.assertAlmostEqual(vision.max_range, 10.0, 1)
        self.assertAlmostEqual(vision.max_fov, 20.0, 1)
