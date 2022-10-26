#!/usr/bin/python3
"""
"""
from datetime import datetime
import os
from models.base_model import BaseModel
from os import path
import unittest


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        """Test Id attribute"""
        _id = type(BaseModel().id)
        self.assertEqual(str, _id)

    def test_currented_at(self):
        """Test currented_at attribute"""
        date = datetime
        self.assertEqual(date, type(BaseModel().created_at))

    def test_updated_at(self):
        """Test updated_at attribute"""
        date = datetime
        self.assertEqual(date, type(BaseModel().updated_at))

    def test_save(self):
        """Test save updated_at"""
        bm = BaseModel()
        bm.save()
        self.assertTrue(path.exists("objects.json"))
        os.remove("objects.json")

        create = BaseModel()
        update = BaseModel()
        self.assertNotEqual(create.created_at,
                            update.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        base = BaseModel()
        self.assertEqual(base.to_dict()['__class__'], base.__class__.__name__)

    def test_str(self):
        """ Test __str__ method """
        base = BaseModel().__str__()
        _str = BaseModel().__str__()
        self.assertNotEqual(_str, base)


if __name__ == "__main__":
    unittest.main()
