#!/usr/bin/python3
"""Unit tests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after each test."""
        del self.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test BaseModel initialization."""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Test save method."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_str(self):
        """Test __str__ method."""
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_file_storage(self):
        """Test FileStorage integration."""
        self.model.save()
        from models import storage
        storage.reload()
        objs = storage.all()
        self.assertIn(self.model.__class__.__name__ + '.' + self.model.id, objs)


if __name__ == "__main__":
    unittest.main()
