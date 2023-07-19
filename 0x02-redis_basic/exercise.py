#!/usr/bin/env python3

"""
This module contains a cache file that uses REDIS
"""

# imports
import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """ Get method for the cache """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)
    
    def get_str(self, key: bytes) -> str:
        """ Parametrize to string """
        return str((key).decode('utf-8'))
    
    def get_int(self, key: bytes) -> int:
        """ Parametrize to integer """
        return int(str(key.decode('utf-8')))
