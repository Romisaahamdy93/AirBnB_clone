# tests/test_file_storage.py
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Remove the file.json if it exists before each test
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        # Create a new FileStorage instance for each test
        self.storage = FileStorage()

    def tearDown(self):
        # Remove the file.json after each test
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        # Test if all() returns the correct dictionary
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        # Test if new() adds an object to the dictionary
        my_model = BaseModel()
        self.storage.new(my_model)
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        # Test if save() and reload() work together correctly
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIn(key, self.storage.all())
        reloaded_model = self.storage.all()[key]
        self.assertEqual(my_model.to_dict(), reloaded_model.to_dict())

if __name__ == '__main__':
    unittest.main()
