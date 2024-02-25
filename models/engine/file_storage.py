#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary or a list of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""