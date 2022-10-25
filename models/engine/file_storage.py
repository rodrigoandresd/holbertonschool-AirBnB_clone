#!/usr/bin/python3
"""
serializes object/instances to a JSON file and deserializes
JSON file to objects/instances
FileStorage class module
"""

import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class module
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionaty __objects """
        return self.__objects
    
    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """ serializes __objects to the JSON file """
        dict_json = {}
        for key, value in self.__objects.items():
            dict_json[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(dict_json))

    def reload(self):
        """  Deserializes the JSON file to __objects """
    