#!/usr/bin/env python3
""" defines all common attributes/methods for other classes """
from uuid import uuid4
from datetime import datetime as dt


class BaseModel:

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ['updated_at', 'created_at']:
                    fromisoformat = dt.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, fromisoformat)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        self.updated_at = dt.now()

    def to_dict(self):
        model = self.__dict__.copy()
        model["__class__"] = self.__class__.__name__
        model["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        model["updated_at"] = self.created_at.isoformat()
        return model
