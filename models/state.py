#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from sqlalchemy.orm import relationship
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            list_cities = []
            for key, value in storage.all(City).items():
                if value.state_id == self.id:
                    list_cities.append(value)
            return list_cities

    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(*args, **kwargs)
