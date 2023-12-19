#!/usr/bin/python3
"""User class definition."""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class Place(BaseModel, Base):
    """Place class for storing place information."""
    __tablename__ = "places"
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class User(BaseModel, Base):
    """User class for storing user information."""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")