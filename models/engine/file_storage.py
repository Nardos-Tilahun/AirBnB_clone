#!/usr/bin/python3
"""
Module that contains class for storage and persistence between """
import json
import os


class FileStorage:
    """
    FileStorage class contains methods and private class attributes """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns all objects that have been saved in the """
        return FileStorage.__objects

    def new(self, obj):
        """
        Create a new dictionary that will most likely be added to the """
        key_name = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key_name] = obj

    def save(self):
        """ new object to the file that stores all the dictionary """
        my_dict = {}
        with open(FileStorage.__file_path, "w", encoding="utf8") as file:
            for key, value in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, file)

    def class_map(self):
        """ Returns a dictionary """
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import BaseModel

        cls_map = {
                "User": User,
                "City": City,
                "State": State,
                "Place": Place,
                "Review": Review,
                "Amenity": Amenity,
                "BaseModel": BaseModel
        }
        return cls_map

    def reload(self):
        """
        reads from a file all serialised objects.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for objs in data.values():
                    cls_key = objs["__class__"]
                    cls_name = self.class_map()[cls_key]
                    self.new(cls_name(**objs))
        except FileNotFoundError:
            pass
