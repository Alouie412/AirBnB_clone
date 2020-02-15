#!/usr/bin/python3
""" This file imports the class from /engine/file_storage.py """
from models.engine.file_storage import FileStorage
""" Creates and reloads the variable storage """


storage = FileStorage()
storage.reload()
