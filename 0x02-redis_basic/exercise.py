#!/usr/bin/env python3

"""
This module contains a cache file that uses REDIS
"""

# imports
import redis
import uuid
from typing import Union


class Cache:
    """A cache class using redis instance"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Stores an object in the redis instance using rand_key from uuid
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key
