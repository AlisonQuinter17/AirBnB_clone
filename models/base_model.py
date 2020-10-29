#!/usr/bin/env python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime
frmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel class."""
    def __init__(self):
        """Constructor."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary.update({'created_at': self.created_at.strftime("frmt")})
        dictionary.update({'updated_at': self.updated_at.strftime("frmt")})
        return dictionary
