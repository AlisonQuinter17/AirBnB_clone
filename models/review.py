#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """ coments by place and user id """
    place_id = ""
    user_id = ""
    text = ""
