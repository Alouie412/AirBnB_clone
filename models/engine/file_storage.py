#!/usr/bin/python3
""" This file imports code from json, datetime, and pathlib """
import json, datetime, os, sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('base_model'))))
sys.path.append('..')
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
        """ All method. Simply returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ New method. Fills in our dictionary """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj.__dict__

    def save(self):
        """ Save method. Saves/serializes the dictionary to our JSON file """
        print("Now testing\n")
        print(self.__objects)
        print("\nThe end\n")
        for key, value in self.__objects.items():
            temp = self.__objects[key]
            print(temp)
            try:
                temp = temp.split(" ")
                temp = temp[2:]
                temp = ' '.join(temp)
                print(temp)
                self.__objects.update({key: temp})
            except:
                print("Failed try")
                #pass

        print("Now Testing again\n")
        print(self.__objects)
        print("\nThe end\n")

        with open(self.__file_path, 'w') as f:
            return json.dump(self.__objects, f,
                             default=lambda x: getattr(x, '__dict__',
                                                       str(x.isoformat())))

    def date_hook(json_dict):
        """ Date_hook method. Used in reload method to convert
        the string in ISO format to datetime format """
        for key, value in json_dict.items():
            try:
                json_dict[key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            except:
                pass
        return json_dict

    def reload(self):
        """ Reload method. Loads/deserializes the dictionary from
        our JSON file """
        import models
        new_dict = {}
        if Path(self.__file_path).is_file():
            with open(self.__file_path, 'r') as f:
                dumped_dict = json.load(f, object_hook=FileStorage.date_hook)
                for key, value in dumped_dict.items():
                    copy = None
                    copy = key.split('.')
                    new_dict[key] = "[{}] ({}) {}".format(copy[0], copy[1], value)
                self.__objects = new_dict
