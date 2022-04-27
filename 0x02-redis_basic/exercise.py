#!/usr/bin/env python3

"""
    Module to learn Redis
"""

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """ blueprint for a redis data storage """
    def __init__(self) -> None:
        """ initializes a Cache instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, float, str, bytes]) -> str:
        """ stores a key-value pair and returns the key """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
