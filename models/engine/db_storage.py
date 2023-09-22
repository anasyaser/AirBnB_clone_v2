#!/usr/bin/python3
"""Module that represents database engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """Data Base engine"""
    __engine = None
    __session = None
    __classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                                      pool_pre_engine=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Get a dictionary for given class, if not given class this function
        will return all instances for all classes
        """
        obj_lst = []
        if cls:
            obj_lst.append(self.__session.query(cls).all())
        else:
            obj_lst.append(self.__session.query(State).all())
            obj_lst.append(self.__session.query(City).all())
            obj_lst.append(self.__session.query(User).all())
            obj_lst.append(self.__session.query(Amenity).all())
            obj_lst.append(self.__session.query(Place).all())
            obj_lst.append(self.__session.query(Review).all())

        obj_dict = {}
        for obj in obj_lst:
            obj_dict["{}.{}".format(type(obj).__name__, obj.id)] = obj

        return obj_dict

    def new(self, obj):
        """Add new object to database"""
        self.__session.add(obj)

    def save(self):
        """Save all changes to databases"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from Database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Get all saved objects"""
        pass
