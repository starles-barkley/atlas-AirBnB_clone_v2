#!/usr/bin/python3
"""Initialize the models package"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

storage_type = os.environ.get('HBNB_TYPE_STORAGE', 'file')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()