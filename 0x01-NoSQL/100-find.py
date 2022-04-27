#!/usr/bin/env python3

"""
    PyMongo: Exercise 7
"""

from pymongo import MongoClient


def find_holberton(school_collection):
    """
        Find all schools whose name start with 'Holberton'
    """
    search_pattern = {"name": {"$regex": "^Holberton"}}
    for school in school_collection.find(search_pattern):
        print(school)


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    school_collection = client.my_db.school
    find_holberton(school_collection)
