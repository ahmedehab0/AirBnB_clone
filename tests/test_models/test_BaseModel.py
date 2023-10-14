#!/usr/bin/python3

import unittest
import sys
sys.path.append("models")
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    """unittest class for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        cls.model1 = BaseModel()
        cls.model2 = BaseModel()

    def test_id(self):
        """test for a uniqe id"""
        self.assertNotEqual(self.model1.id, self.model2.id)
    
    def test_str_method(self):
        """test for the __str__ method"""
        self.model_repr = str(self.model1)
        self.assertEqual(self.model_repr, "[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}")


if __main__ == "__name__" :
    unittest.main()
