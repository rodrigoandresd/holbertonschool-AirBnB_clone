#!/usr/bin/python3
"""
Test file for File Storage
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import path


class TestFileStorage(unittest.TestCase):
    """"""

    def test_filepath(self):
        s = FileStorage()
        storage = s._FileStorage__file_path
        self.assertEqual(storage, "file.json")

    def test_all_method(self):
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)
        self.assertIs(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        storage = FileStorage()
        storage.save()
        storage.reload()
        self.assertTrue(len(storage.all()) > 0)
