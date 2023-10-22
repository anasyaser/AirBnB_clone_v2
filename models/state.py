#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv
from models import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', back_populates='state')

    else:
        @property
        def cities(self):
            """Return list of cities related to the current state"""
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
