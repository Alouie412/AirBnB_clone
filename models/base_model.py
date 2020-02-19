#!/usr/bin/python3
""" This file imports code found in uuid and datetime
as well as the variable storage from __init__.py """
import uuid
import datetime
import models
""" base_model.py """


class BaseModel:
    """ BaseModel class. The foundation for other classes """
    def __init__(self, *args, **kwargs):
        """ Initialization method. Check if kwargs exist. If so,
        set the instance. Otherwise, create a new instance
        """
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value,
                                                       '%Y-%m-%dT%H:%M:%S.%f')
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ String modifier method. Prints the following format """
        return ("[{}] ({}) {}".format(__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """ Save method. Updates the attribute updated_at """
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """ to_dict method. Converts to dictionary format """
        to_new_dict = self.__dict__.copy()
        to_new_dict['created_at'] = self.created_at.isoformat()
        to_new_dict['updated_at'] = self.updated_at.isoformat()
        return to_new_dict
