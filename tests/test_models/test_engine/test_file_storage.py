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

    def test_path(self):
        if path.exists("objects.json"):
            os.remove("objects.json")
        # f = FileStorage()
        # storage = f._FileStorage_.__file_path
        # self.assertEqual(storage, 'objects.json')
