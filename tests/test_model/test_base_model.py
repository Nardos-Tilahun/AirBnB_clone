#!usr/bin/python3
"""
this a test for base model
"""
import unittest
from models.base_model import BaseModel

class TestBasemodel(unittest.TestCase):
    """class that test the Base model

    Args:
        unittest (TestCase): _description_: it is used to test the model in the python
    """
    
    def test_init(self):
        """this used to test the constractor of teh baseModel that inistialte all the object form the class
        """
        en_model = BaseModel()
        
        self.assertIsNotNone(en_model.id)
        self.assertIsNotNone(en_model.created_at)
        self.assertIsNotNone(en_model.updated_at)
    
    def test_save(self):
        """
        This test the save method in the BaseModel
        """
        en_model = BaseModel()
        
        first_update = en_model.updated_at
        
        second_update = en_model.save();
        
        
        self.assertNotEqual(first_update, second_update)
        
    def test_to_dict(self):
        """
        checking/testing the dictionary method of the instance
        """
        en_model = BaseModel();
        
        en_model_dict = en_model.to_dict();
        
        self.assertIsInstance(en_model_dict, dict)
        
        self.assertEqual(en_model_dict["__class__"], "BaseModel")
        self.assertEqual(en_model_dict["id"], en_model.id)
        self.assertEqual(en_model_dict['created_at'], en_model.created_at.isoformat())
        self.assertEqual(en_model_dict['updated_at'], en_model.updated_at.isoformat())
        
    def test_str(self):
        """
        checking or testing the string representation of the instance of the BaseModel
        """
        
        en_model = BaseModel()
        
        self.assertTrue(str(en_model).startswith('[BaseModel]'))
        self.assertIn(en_model.id, str(en_model))
        self.assertIn(str(en_model.__dict__), str(en_model))
        
if __name__ == '__main__':
    unittest.main()
        
        
        