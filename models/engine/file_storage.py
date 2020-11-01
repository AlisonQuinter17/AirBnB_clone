#!/usr/bin/env python3
"""Module for FileStorage class."""
import json


class FileStorage:
    """FileStorage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary: '__objects'."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes(convert a object to string) the dictionary:
        '__objects' to the JSON file: '__file_path'.
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({key: value.to_dict() for key, value in
                       self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes(convert a string to an object) the JSON file:
        '__file_path' to a dictionary: '__objects', in case the JSON
        file doesn't exist, it does nothing.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                the_dict = json.loads(f.read())
                for value in the_dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
