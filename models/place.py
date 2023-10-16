#!/usr/bin/python3

""" Place class for our HBnB clone  project """

from models.base_model import BaseModel


class Place(BaseModel):

    """
    Repr a place.

    Attrs:
        city_id (str): ciity id.
        user_id (str): user id.
        name (str): name of the place.
        description (str): desc of the place.
        number_rooms (int): num of rooms available.
        number_bathrooms (int): num of bathrooms available.
        max_guest (int): max num of expected guests.
        price_by_night (int): price/cost per night.
        latitude (float): lat of the facility.
        longitude (float): long of the facility.
        amenity_ids (list): list of Amenity ids.

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
