#!/usr/bin/python3
"""
Test file for File Storage
"""
import unittest

import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import path



class TestFileStorage(unittest.TestCase):
    """"""


    def test_all_method(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

