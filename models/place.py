#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review',
                               backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity',
                                 secondary='place_amenity',
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id
               equals to the current Place.id"""
            from models.review import Review
            from models import storage
            list_reviews = []
            all_reviews = storage.all(Review)
            for value in all_reviews.values():
                if value.place_id == self.id:
                    list_reviews.append(value)
            return list_reviews

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on the
               attibute amenity_ids that contains all Amenity.id"""
            from models.amenity import Amenity
            from models import storage
            list_amenities = []
            all_amenities = storage.all(Amenity)
            for value in all_amenities.values():
                if value.place_id == self.id:
                    list_amenities.append(value)
            return list_amenities

        @amenities.setter
        def amenities(self, value):
            """"Handles append method for adding an Amenity.id to the
                attribute amenity_ids"""
            from models import storage
            if type(value) == 'Amenity':
                self.amenity_ids.append(value.id)
