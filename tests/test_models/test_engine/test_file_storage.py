#!/usr/bin/python3
"""
Test file for File Storage
"""
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import path
import unittest


class TestFileStorage(unittest.TestCase):
    """"""

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

if __name__ == '__main__':
    unittest.main()