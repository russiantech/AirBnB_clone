#!/usr/bin/python3

""" User class for our HBnB clone project. """

from models.base_model import BaseModel


class User(BaseModel):

    """
    Repr a User.
    Attributes:
        email (str): user's email address.
        password (str): user's password.
        first_name (str): user's 1st name.
        last_name (str): user's last name.

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
