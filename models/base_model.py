#!/usr/bin/python3

""" HBnB BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    """ Repr BaseModel of the HBnB project. """

    def __init__(self, *args, **kwargs):

        """

	Inits new BaseModel.

        Args:
            *args (any): not used.
            **kwargs (dict): Key:value pairs of attrs.

        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):

        """ Updates the time to current date in db/storage """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):

        """ 
	Returns the dict of the BaseModel instance.
        with key/value pair __class__ repr..ing
        the class name of the object.
        """

        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__

        return rdict

    def __str__(self):

        """ Returns print/str repr of the BaseModel instance."""

        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
