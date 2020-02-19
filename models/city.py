#!/usr/bin/python3
""" city.py """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class. Inherits BaseModel """
    state_id = ""
    name = ""
