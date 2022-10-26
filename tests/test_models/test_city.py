#!/usr/bin/python3
"""
Test for City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Initialization class"""

    def test_state_id(self):
        """Test for test id attribute"""
        cty = City()
        self.assertEqual(cty.state_id, "")

    def test_name_state(self):
        """Test for name attribute"""
        cty = City()
        self.assertEqual(cty.name, "")
