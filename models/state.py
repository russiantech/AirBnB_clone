#!/usr/bin/python3

""" State class for our HBnB clone project"""

from models.base_model import BaseModel


class State(BaseModel):

    """
    Repr a state.

    Attr:
        name (str): the state name.
    """

    name = ""
