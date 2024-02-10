#!/usr/bin/python3
"""Test City class."""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test the City class."""

    def test_city_instance(self):
        """Test City instance creation."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertEqual(type(city.id), str)
        self.assertEqual(type(city.created_at), type(city.updated_at))

    def test_city_str(self):
        """Test City __str__ method."""
        city = City()
        self.assertEqual(str(city), "[City] ({}) {}".format(city.id, city.__dict__))

if __name__ == "__main__":
    unittest.main()
