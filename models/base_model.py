#!/usr/bin/python3
"""
"""
from datetime import datetime
import uuid


class BaseModel:
    """ BaseModel class """

    def __init__(self):
        """"initialize variables and methods"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """
        method that returns a string representation
        """

        cls_name = self.__class__.__name__
        msg_format = "[{}] ({}) {}"
        return msg_format.format(cls_name, self.id, self.__dict__)

    def save(self):
        """
        method that updates the public instance attribute updated_at
        with the current datetime
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        method that returns adictionaty containing all key/values of __dict__
        """
        dict_return = self.__dict__.copy()
        dict_return["__class__"] = self.__class__.__name__
        dict_return["created_at"] = self.created_at.isoformat()
        dict_return["updated_at"] = self.update_at.isoformat()

        return dict_return
