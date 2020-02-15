#!/usr/bin/python3
""" This file imports code found in uuid and datetime
as well as the variable storage from __init__.py """
import uuid
import datetime
from models.__init__ import storage
""" base_model.py """


class BaseModel:
    """ BaseModel class. The foundation for other classes """
    def __init__(self, *args, **kwargs):
        """ Initialization method. Creates 5 objects.
        Supports args and kwargs, as well as conversion between string
        and datetime. Also creates a new instance """
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key in "id":
                    self.id = value
                elif key in "created_at":
                    self.created_at = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key in "updated_at":
                    self.updated_at = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key in "my_number":
                    self.my_number = value
                elif key in "name":
                    self.name = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            self.my_number = 0
            self.name = ""
            storage.new(self)

    def __str__(self):
        """ String modifier method. Prints the following format """
        return ("[{}] ({}) {}".format(__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """ Save method. Updates the attribute updated_at """
        self.updated_at = datetime.datetime.today()
        storage.save()

    def to_dict(self):
        """ to_dict method. Converts to dictionary format """
        self.__dict__ = {'my_number': self.my_number, 'name': self.name,
                         '__class__': __class__.__name__,
                         'updated_at': str(self.updated_at.isoformat()),
                         'id': self.id,
                         'created_at': str(self.created_at.isoformat())}
        return self.__dict__
