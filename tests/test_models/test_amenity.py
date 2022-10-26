#!/usr/bin/python3
"""
Test for Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Initialization class"""

    def test_name(self):
        """Test for name attribute"""
        amy = Amenity()
        self.assertEqual(amy.name, "")
