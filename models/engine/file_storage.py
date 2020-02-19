#!/usr/bin/python3
""" This file imports code from json, datetime, and pathlib """
import json, datetime, os, sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('base_model'))))
sys.path.append('..')
from pathlib import Path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
""" FileStorage class. Stores stuff into a JSON file """


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ All method. Simply returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ New method. Fills in our dictionary """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ Save method. Saves/serializes the dictionary to our JSON file """
        with open(self.__file_path, 'w') as f:
            new_dict = {key: obj.to_dict() for key, obj in
                        self.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """ Reload method. Loads/deserializes the dictionary from
        our JSON file """
        if Path(self.__file_path).is_file():
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(key.split('.')[0])(**value)
