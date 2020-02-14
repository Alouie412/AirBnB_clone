#!/usr/bin/python3
""" This file imports code found in uuid and datetime """
import uuid
import datetime
""" BaseModel class. The foundation for other classes """


class BaseModel:
    """ BaseModel class initialization. Creates 5 objects """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        self.my_number = 0
        self.name = ""

    def __str__(self):
        """ String modifier method """
        return ("[{}] ({}) {}".format(__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """ Save method. Updates the attribute updated_at """
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """ to_dict method. Converts to dictionary format """
        self.__dict__ = {'my_number': self.my_number, 'name': self.name,
                         '__class__': __class__.__name__,
                         'updated_at': str(self.updated_at.isoformat()),
                         'id': self.id,
                         'created_at': str(self.created_at.isoformat())}
        return self.__dict__
