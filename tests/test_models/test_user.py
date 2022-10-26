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
        u.email = "luiyi@example.com"
        self.assertEqual(u.email, "luiyi@example.com")

    def test_password(self):
        """Test for password attribute"""
        u = User()
        u.password = "pwd"
        self.assertEqual(u.password, "pwd")

    def test_first_name(self):
        """Test for fitst name attribute"""
        u = User()
        u.first_name = "Rodrigo"
        self.assertEqual(u.first_name, "Rodrigo")

    def test_last_name(self):
        """Test for last name attribute"""
        u = User()
        u.last_name = "Duque"
        self.assertEqual(u.last_name, "Duque")
