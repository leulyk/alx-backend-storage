#!/usr/bin/env python3

"""
    PyMongo: exercise 4
"""


def schools_by_topic(mongo_collection, topic):
    """ returns a list of schools teaching a specified topic """
    matches = []
    for school in mongo_collection.find():
        print(school)
        if "Python" in school["topics"]:
            matches.append(school)
    return matches
