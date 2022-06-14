#!/usr/bin/env python3

"""
    PyMongo: Exercise 8
"""


def top_students(mongo_collection):
    """ return students sorted by average score """
    return mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ])
