#!/usr/bin/python3
""" Definition of the Place class and its attributes """

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models

# Define a table for the many-to-many relationship between Place and Amenity
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))

# Define the Place class


class Place(BaseModel, Base):
    """ Class representing a place with various attributes """

    # Define the table name
    __tablename__ = "places"

    # Define columns and their data types
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    # Define relationships based on the storage type
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        # Define properties for non-database storage
        @property
        def reviews(self):
            """Returns a list of reviews associated with the place"""
            var = models.storage.all()
            lista = [var[key] for key in var if key.replace('.', ' ').split()[
                0] == 'Review']
            return [elem for elem in lista if elem.place_id == self.id]

        @property
        def amenities(self):
            """Returns a list of amenity ids associated with the place"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Appends amenity ids to the attribute"""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
