#!/usr/bin/env python3

"""
    PyMongo test
"""


def list_all(mongo_collection):
    """ return the list all documents in a collection """
    return mongo_collection.find()
