#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # For FileStorage
    @property
    def cities(self):
        """Getter attribute for cities in FileStorage"""
        from models import storage
        all_cities = storage.all("City")
        return [city for city in all_cities.values() if city.state_id == self.id]
