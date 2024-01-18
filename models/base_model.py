#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
<<<<<<< HEAD
    """ Defines a class Basemodel """
=======
    """Represents the BaseModel of the HBnB project."""

>>>>>>> 1f1bc1b4cbd670da00e3348f286c4e3978fa470e
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
<<<<<<< HEAD
        """ updated_at' attribute to the current datetime """
        
        self.updated_at = datetime.now()  # when it was last updated
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary representation """
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        # iterate, extract & convert datetime values to a str in ISO format
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return dict(my_dict)

    def __str__(self):
        """Helpful for debugging and such """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
            )
=======
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

>>>>>>> 1f1bc1b4cbd670da00e3348f286c4e3978fa470e
