#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a State for the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize a new State."""
        super().__init__(*args, **kwargs)
        self.name = ""


    def __str__(self):
        """Return the print/str representation of the State instance."""
        return "[State] ({}) {}".format(self.id, self.__dict__)

