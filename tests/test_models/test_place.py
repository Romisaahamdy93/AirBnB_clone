#!/usr/bin/python3
"""Test Place class."""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test the Place class."""

    def test_place_instance(self):
        """Test Place instance creation."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        self.assertEqual(type(place.id), str)
        self.assertEqual(type(place.created_at), type(place.updated_at))

    def test_place_str(self):
        """Test Place __str__ method."""
        place = Place()
        self.assertEqual(str(place), "[Place] ({}) {}".format(place.id, place.__dict__))

if __name__ == "__main__":
    unittest.main()
