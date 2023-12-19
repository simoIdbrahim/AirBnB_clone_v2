#!/usr/bin/python3
"""Place class definition."""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """Place class for storing place information."""
    __tablename__ = "places"
    # Define Place class columns and attributes here


class Review(BaseModel, Base):
    """Review class for storing review information."""
    __tablename__ = "reviews"
    # Define Review class columns and attributes here


class User(BaseModel, Base):
    """User class for storing user information."""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")
