#!/usr/bin/python3

"""
serializes object/instances to a JSON file and deserializes
JSON file to objects/instances
FileStorage class module
"""

import json
import os.path

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
        key = obj.__class__.__name__, obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        dict_json = {}
        for key, value in self.__objects.items():
            dict_json[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(dict_json))

    def reload(self):
        """  Deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                json_object = json.loads(file.read())

                for key, value in json_object.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
