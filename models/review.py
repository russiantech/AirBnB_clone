#!/usr/bin/python3

""" Review class for our HBnB cloee project """

from models.base_model import BaseModel


class Review(BaseModel):

    """

    Repr a review.
    Attributes:
        place_id (str): place id.
        user_id (str): user id.
        text (str): review text.

    """

    place_id = ""
    user_id = ""
    text = ""
