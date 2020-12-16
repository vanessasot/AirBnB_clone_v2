#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    if storage_type == "bd":
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            _cities_list = []
            all_cities = models.storage.all(City)
            for city_id, obj in all_cities.items():
                if self.id == obj.state_id:
                    _cities_list.append(obj)
            return _cities_list
