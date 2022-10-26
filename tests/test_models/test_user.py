#!/usr/bin/python3
"""
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    TestUser Clas
    """

    def test_email(self):
        """Test for email attribute"""
        u = User()
        self.assertEqual(u.email, "")

    def test_password(self):
        """Test for password attribute"""
        u = User()
        self.assertEqual(u.password, "")

    def test_first_name(self):
        """Test for fitst name attribute"""
        u = User()
        self.assertEqual(u.first_name, "")

    def test_last_name(self):
        """Test for last name attribute"""
        u = User()
        self.assertEqual(u.last_name, "")
