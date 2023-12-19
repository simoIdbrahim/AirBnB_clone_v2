#!/usr/bin/python3
"""SQLAlchemy database storage class."""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ Create and manage SQLAlchemy tables based on environment. """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the database storage. """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return a dictionary of objects. """
        obj_dict = {}

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                obj_dict[key] = elem
        else:
            class_list = [State, City, User, Place, Review, Amenity]
            for model_class in class_list:
                query = self.__session.query(model_class)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    obj_dict[key] = elem

        return obj_dict

    def new(self, obj):
        """ Add a new element to the table. """
        self.__session.add(obj)

    def save(self):
        """ Save changes. """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete an element from the table. """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Configure and reload the database. """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scoped_session_instance = scoped_session(session)
        self.__session = scoped_session_instance()

    def close(self):
        """ Close the session. """
        self.__session.close()
