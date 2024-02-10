#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City for the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize a new City."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

    def __str__(self):
        """Return the print/str representation of the City instance."""
        return "[City] ({}) {}".format(self.id, self.__dict__)
