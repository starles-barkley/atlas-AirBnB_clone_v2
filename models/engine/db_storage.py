#!/usr/bin/python3
"""This module defines a class DBStorage for the storage engine"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from os import environ as env


class DBStorage:
    """This class defines the MySQL database storage engine."""
    __engine = None
    __session = None

    def __init__(self):
        """Creates an instance of DBStorage."""
        self.__engine = create_engine(connect, pool_pre_ping=True)
        self.__session = sessionmaker(bind=self.__engine)
        if environment == 'test':
            db_metadata.drop_all()
            
    def all(self, cls=None):
        """Query on the current database session."""
        from models import base_model
        classes = [base_model.User, base_model.State, base_model.City,
                   base_model.Amenity, base_model.Place, base_model.Review]

        objects = {}
        if cls:
            classes = [cls]

        for cls in classes:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj

        return objects
