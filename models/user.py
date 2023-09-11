#!/usr/bin/python3
""" holds class User"""
import models
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    """Representation of a user """
    __tablename__ = 'users'

    name = Column(String(50), nullable=False)
    user_id = Column(Integer, primary_key=True)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
