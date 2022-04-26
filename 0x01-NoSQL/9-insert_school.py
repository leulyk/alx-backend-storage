#!/usr/bin/env python3

"""
    PyMongo Exercise #2
"""


def insert_school(mongo_collection, **kwargs):
    """ inserts an object to a collection """
    new_obj = mongo_collection.insert_one(kwargs)
    return new_obj.inserted_id
