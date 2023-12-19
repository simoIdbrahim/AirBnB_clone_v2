#!/usr/bin/python3
"""User class definition."""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """User class for storing user information.

    Attributes:
        email (str): Email address of the user.
        password (str): Password for user login.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        places (relationship): One-to-many relationship with Place.
        reviews (relationship): One-to-many relationship with Review.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
