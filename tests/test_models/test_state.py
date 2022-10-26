#!/usr/bin/python3
"""
Test for State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Initialization class"""

    def test_name_state(self):
        """Test for name attribute"""
        st = State()
        self.assertEqual(st.name, "")
