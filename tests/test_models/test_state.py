#!/usr/bin/python3
"""Test State class."""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test the State class."""

    def test_state_instance(self):
        """Test State instance creation."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")
        self.assertEqual(type(state.id), str)
        self.assertEqual(type(state.created_at), type(state.updated_at))

    def test_state_str(self):
        """Test State __str__ method."""
        state = State()
        self.assertEqual(str(state), "[State] ({}) {}".format(state.id, state.__dict__))

if __name__ == "__main__":
    unittest.main()
