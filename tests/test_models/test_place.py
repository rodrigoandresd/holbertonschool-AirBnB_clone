#!/usr/bin/python3
"""
Test for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Initialization class"""

    def test_city_id(self):
        """Test for city id attribute"""
        plc = Place()
        self.assertEqual(plc.city_id, "")

    def test_user_id(self):
        """Test for user id attribute"""
        plc = Place()
        self.assertEqual(plc.user_id, "")

    def test_name(self):
        """Test for name attribute"""
        plc = Place()
        self.assertEqual(plc.name, "")

    def test_description(self):
        """Test for description attribute"""
        plc = Place()
        self.assertEqual(plc.description, "")

    def test_num_rooms(self):
        """Test for number number rooms"""
        plc = Place()
        self.assertEqual(plc.number_rooms, 0)

    def test_num_bathrooms(self):
        """Test for number bathrooms attribute"""
        plc = Place()
        self.assertEqual(plc.number_bathrooms, 0)

    def test_max_guest(self):
        """Test for number max guest attribute"""
        plc = Place()
        self.assertEqual(plc.max_guest, 0)

    def test_price_by_night(self):
        """Test for price by night attribute"""
        plc = Place()
        self.assertEqual(plc.price_by_night, 0)

    def test_latitude(self):
        """Test for latitude attribute"""
        plc = Place()
        self.assertEqual(plc.latitude, 0.0)

    def test_longitude(self):
        """Test for longitude attribute"""
        plc = Place()
        self.assertEqual(plc.longitude, 0.0)

    def test_amenity_ids(self):
        """Test for amenity ids attribute"""
        plc = Place()
        self.assertEqual(plc.amenity_ids, [])
