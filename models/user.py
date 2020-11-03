#!/usr/bin/python3
""" inherits from Base model """
from models.basemodel import BaseModel


class User(BaseModel):
    """ holds user info """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
