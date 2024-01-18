#!/usr/bin/python3
"""
This is the module for basemodel.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    The BaseModel class that define common properties of the classes
    """
    
    def __init__(self, *args, **kwargs):
        """
        This method initiate the object as a constractor
        """
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        
    def save(self):
        """
            used to save the the object at the current date time
        """
        self.updated_at = datetime.now();
    
    def to_dict(self):
        """
        return dictionary of the instances
        """
        inst_dict = self.__dict__.copy();
        inst_dict["__class__"] = self.__class__.__name__;
        inst_dict["created_at"] = self.created_at.isoformat();
        inst_dict["updated_at"] = self.updated_at.isoformat();
        
        return inst_dict

    def __str__(self):
        """generate the string representation of the instance
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
            
if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))