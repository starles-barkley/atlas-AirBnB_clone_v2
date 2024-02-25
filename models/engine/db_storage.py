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
        res = {}
        if cls is None:
            query = self.__session.query().all()
        else:
            query = self.__session.query(cls).all()
