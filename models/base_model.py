#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datatime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

def __str__(self):
    return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

def save(self):
    self.updated_at = datetime.now()


def to_dict(self):
    model_dict = self.__dict__.copy()
    model_dict['__class__'] = self.__class__.__name__
    model_dict['created_at'] = self.created_at.isoformat()
    model_dict['updated_at'] = self.updated_at.isoformate()
    return model_dict
