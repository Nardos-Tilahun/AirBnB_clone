#!/usr/bin/python3

"""
module contains the BaseModel class that all other classses
"""
import models
from uuid import uuid4
from datetime import datetime
# from models import storage


class BaseModel:
    """ Defines a class Basemodel """
    def __init__(self, *args, **kwargs):
        """ Initialises all public object attribute """

        if kwargs:
            del kwargs["__class__"]
            for keys, value in kwargs.items():
                if keys == "updated_at" or keys == "created_at":
                    # convert its value (previously a str) to datetime object
                    dt_time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, keys, dt_time)
                else:
                    setattr(self, keys, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
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
