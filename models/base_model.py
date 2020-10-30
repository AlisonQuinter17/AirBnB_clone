#!/usr/bin/env python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime


class BaseModel():
    """BaseModel class."""
    def __init__(self, *args, **kwargs):
        """
        Arguments
          - *args: is a Tuple that contains all arguments (won’t be used).
          - **kwargs: is a dictionary that contains all arguments by key/value.

        Functions/methods:
          - strptime(): creates a datetime object from the given string.
          - setattr(): sets the value of the attribute of an object.
        """

        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    pass
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.
                            strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Used to find the human readable or "informal" string
        representation of an object.
        """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary.update({'created_at': self.created_at.isoformat()})
        dictionary.update({'updated_at': self.updated_at.isoformat()})
        return dictionary
