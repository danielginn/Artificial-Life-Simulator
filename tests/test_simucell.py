from unittest import TestCase
from simucell import SimuCell
import numpy as np
from world import World

class TestSimuCell(TestCase):
    def test_should_move_1_meter_right(self):
        expectedDestination = np.array([1.0, 0.0])
        blob = SimuCell(world=World(), initLocation=np.array([0.0, 0.0]), initHeading=0.0)
        blob.speed = 1.0
        blob.update_location()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)

    def test_should_move_1_meter_down(self):
        expectedDestination = np.array([0.0, 1.0])
        blob = SimuCell(world=World(), initLocation=np.array([0.0, 0.0]), initHeading=90.0)
        blob.speed = 1.0
        blob.update_location()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)

    def test_should_move_1_meter_diagonally_SE(self):
        expectedDestination = np.array([0.707, 0.707])
        blob = SimuCell(world=World(), initLocation=np.array([0.0, 0.0]), initHeading=45.0)
        blob.speed = 1.0
        blob.update_location()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)

    def test_should_move_2_meters_to_right(self):
        expectedDestination = np.array([2.0, 0.0])
        blob = SimuCell(world=World(), initLocation=np.array([0.0, 0.0]), initHeading=0.0)
        blob.speed = 2.0
        blob.update_location()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)

    def test_should_move_2_meters_diagonally_NE(self):
        expectedDestination = np.array([1.414, 1.414])
        blob = SimuCell(world=World(), initLocation=np.array([0.0, 0.0]), initHeading=45.0)
        blob.speed = 2.0
        blob.update_location()
        np.testing.assert_almost_equal(blob.location, expectedDestination, decimal=1)

    def test_should_bounce_directly_off_walls(self):
        blob = SimuCell(world=World(), initLocation=np.array([0.0, 0.0]), initHeading=0.0)
        blob.speed = 10.0
        startingLocations = [np.array([5.0, 5.0]), np.array([5.0, 5.0]), np.array([795.0, 595.0]), np.array([795.0, 595.0])]
        startingHeadings = [-90.0, 180.0, 90.0, 0.0]
        expectedDestinations = [np.array([5.0, 15.0]), np.array([15.0, 5.0]), np.array([795.0, 585.0]), np.array([785.0, 595.0])]

        for i in range(len(startingLocations)):
            blob.location = startingLocations[i]
            blob.heading = startingHeadings[i]
            blob.update_location()
            np.testing.assert_almost_equal(blob.location, expectedDestinations[i], decimal=1)

    def test_should_bounce_diagonally_off_walls(self):
        blob = SimuCell(world=World(), initLocation=np.array([0.0, 0.0]), initHeading=0.0)
        blob.speed = 14.14
        startingLocations = [np.array([5.0, 5.0]), np.array([5.0, 5.0]), np.array([795.0, 595.0]), np.array([795.0, 595.0])]
        startingHeadings = [135.0, -45.0, 135.0, -45.0]
        expectedDestinations = [np.array([15.0, 15.0]), np.array([15.0, 15.0]), np.array([785.0, 585.0]), np.array([785.0, 585.0])]

        for i in range(len(startingLocations)):
            blob.location = startingLocations[i]
            blob.heading = startingHeadings[i]
            blob.update_location()
            np.testing.assert_almost_equal(blob.location, expectedDestinations[i], decimal=1)

    def test_should_bounce_diagonally_off_corners(self):
        blob = SimuCell(world=World(), initLocation=np.array([0.0, 0.0]), initHeading=0.0)
        blob.speed = 14.14
        startingLocations = [np.array([5.0, 5.0]), np.array([795.0, 5.0]), np.array([795.0, 595.0]), np.array([5.0, 595.0])]
        startingHeadings = [-135.0, -45.0, 45.0, 135.0]
        expectedDestinations = [np.array([15.0, 15.0]), np.array([785.0, 15.0]), np.array([785.0, 585.0]), np.array([15.0, 585.0])]

        for i in range(len(startingLocations)):
            blob.location = startingLocations[i]
            blob.heading = startingHeadings[i]
            blob.update_location()
            np.testing.assert_almost_equal(blob.location, expectedDestinations[i], decimal=1)