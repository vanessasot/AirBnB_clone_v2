#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """DB Storage class"""
    __engine = None
    __session = None

    def __init__(self):
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(username,
                                              password,
                                              host,
                                              db_name),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            # Metadata is an instance inside the Base and drop_all
            # is a method inside metadata
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        get all rows based on class
        """
        class_objects = {}
        if cls is None:
            objects = self.__session.query(State, City)
            for obj in objects:
                key = type(obj).__name__ + "." + str(obj.id)
                class_objects[key] = obj
                # return class_objects with all class objects
        else:
            objects = self.__session.query(eval(cls)).all()
            for obj in objects:
                key = type(obj).__name__ + "." + str(obj.id)
                class_objects[key] = obj

        return class_objects

    def new(self, obj):
        """
        add instance
        """
        self.__session.add(obj)

    def save(self):
        """
        commit changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        reload sql tables
        create session
        """
        Base.metadata.create_all(self.__engine)
        # scoped_session() function is provided which produces a thread-managed
        # registry of Session objects.
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """
        close session
        """
        self.__session.close()
