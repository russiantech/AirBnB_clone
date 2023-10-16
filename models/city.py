#!/usr/bin/python3

"""City class."""

from models.base_model import BaseModel


class City(BaseModel):

    """
    Repr a city.
    Attr:
        state_id (str): listedcity/state id.
        name (str): listed city name.

    """

    state_id = ""

    name = ""
