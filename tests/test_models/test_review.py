#!/usr/bin/python3
"""
Test for Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Initialization class"""

    def test_place_id(self):
        """Test for place id attribute"""
        rw = Review()
        self.assertEqual(rw.place_id, "")

    def test_user_id(self):
        """Test for user id attribute"""
        rw = Review()
        self.assertEqual(rw.user_id, "")

    def test_text(self):
        """Test for text attribute"""
        rw = Review()
        self.assertEqual(rw.text, "")
