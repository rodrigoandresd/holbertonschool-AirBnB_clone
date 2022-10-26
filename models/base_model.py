#!/usr/bin/python3
"""
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Method __init__ initialize the all attibutes """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        method that returns adictionaty containing all key/values of __dict__
        """
        dict_return = self.__dict__.copy()
        dict_return["__class__"] = self.__class__.__name__
        dict_return["created_at"] = self.created_at.isoformat()
        dict_return["updated_at"] = self.updated_at.isoformat()

        return dict_return
