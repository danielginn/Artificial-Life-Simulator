from unittest import TestCase
from simucell import SimuCell
import numpy as np

class TestSimuCell(TestCase):
    def test_should_move_1_meter_right(self):
        expectedDestination = np.array([1.0, 0.0])
        blob = SimuCell(initLocation=np.array([0.0, 0.0]), initHeading=0.0)
        blob.speed = 1.0
        blob.updateLocation()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)

    def test_should_move_1_meter_down(self):
        expectedDestination = np.array([0.0, 1.0])
        blob = SimuCell(initLocation=np.array([0.0, 0.0]), initHeading=90.0)
        blob.speed = 1.0
        blob.updateLocation()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)

    def test_should_move_1_meter_diagonally_SE(self):
        expectedDestination = np.array([0.707, 0.707])
        blob = SimuCell(initLocation=np.array([0.0, 0.0]), initHeading=45.0)
        blob.speed = 1.0
        blob.updateLocation()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)

    def test_should_move_2_meters_to_right(self):
        expectedDestination = np.array([2.0, 0.0])
        blob = SimuCell(initLocation=np.array([0.0, 0.0]), initHeading=0.0)
        blob.speed = 2.0
        blob.updateLocation()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)

    def test_should_move_2_meters_diagonally_NE(self):
        expectedDestination = np.array([1.414, 1.414])
        blob = SimuCell(initLocation=np.array([0.0, 0.0]), initHeading=45.0)
        blob.speed = 2.0
        blob.updateLocation()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)