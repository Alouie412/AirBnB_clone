#!/usr/bin/python3
""" This file imports code from json and pathlib """
import json
from pathlib import Path
""" FileStorage class. Stores stuff into a JSON file """


class FileStorage:
    """ FileStorage class """
    def __init__(self):
        """ Initialization method. Designates file to be saved to
        and creates an empty dictionary """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ All method. Simply returns the dictionray """
        return self.__objects

    def new(self, obj):
        """ New method. Fills in our dictionary """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj.__dict__

    def save(self):
        """ Save method. Saves/serializes the dictionary to our JSON file """
        with open(self.__file_path, 'w') as f:
            return json.dump(self.__objects, f,
                             default=lambda x: getattr(x, '__dict__',
                                                       str(x.isoformat())))

    def reload(self):
        """ Reload method. Loads/deserializes the dictionary from
        our JSON file """
        if Path(self.__file_path).is_file():
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
