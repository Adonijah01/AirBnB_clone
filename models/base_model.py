#!/usr/bin/python3
"""Module for Base class
Containng the Base class for AirBnB console.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Class for base model of hierarchy of object."""

    def __init__(self, *args, **kwargs):
        """Initialization of  Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dicttionary of key-value arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return human
        readable string rep
        of a instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updatd attribute
        with current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary rep of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

    """Adonijah Kiplimo & Betty jelagat"""
