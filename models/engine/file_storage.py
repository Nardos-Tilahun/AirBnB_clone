#!/usr/bin/python3
<<<<<<< HEAD
"""
Module that contains class for storage and persistence between """
=======
"""Defines the FileStorage class."""
>>>>>>> 1f1bc1b4cbd670da00e3348f286c4e3978fa470e
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
<<<<<<< HEAD
    """
    FileStorage class contains methods and private class attributes """
=======
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
>>>>>>> 1f1bc1b4cbd670da00e3348f286c4e3978fa470e
    __file_path = "file.json"
    __objects = {}

    def all(self):
<<<<<<< HEAD
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
=======
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
>>>>>>> 1f1bc1b4cbd670da00e3348f286c4e3978fa470e
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

