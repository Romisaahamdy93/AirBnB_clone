#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):

def test_instance_attributes(self):
my_model = BaseModel()
self.assertTrue(hasattr(my_model, 'id'))
self.assertTrue(hasattr(my_model, 'created_at'))
self.assertTrue(hasattr(my_model, 'updated_at'))

def test_str_method(self):
my_model = BaseModel()
expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
self.assertEqual(str(my_model), expected_str)

def test_save_method(self):
my_model = BaseModel()
original_updated_at = my_model.updated_at
my_model.save()
self.assertNotEqual(original_updated_at, my_model.updated_at)

def test_to_dict_method(self):
my_model = BaseModel()
model_dict = my_model.to_dict()

self.assertIsInstance(model_dict, dict)
self.assertEqual(model_dict['__class__'], 'BaseModel')
self.assertEqual(model_dict['id'], my_model.id)
self.assertEqual(model_dict['created_at'], my_model.created_at.isoformat())
self.assertEqual(model_dict['updated_at'], my_model.updated_at.isoformat())

def test_json_representation(self):
my_model = BaseModel()
my_model_json = my_model.to_dict()
json_str = json.dumps(my_model_json)
expected_json_str = '{"__class__": "BaseModel", "id": "' + my_model.id + '", "created_at": "' + my_model.created_at.isoformat() + '", "updated_at": "' + my_model.updated_at.isoformat() + '"}'
self.assertEqual(json_str, expected_json_str)


if __name__ == '__main__':
unittest.main()

