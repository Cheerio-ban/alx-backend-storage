#!/usr/bin/env python3

"""
This module contains a cache file that uses REDIS
"""

# imports
import redis
import uuid
from functools import wraps
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """count the number of times a functon is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function for a function decorator"""
        key = method.__qualname__
        data = self._redis.get(key)
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store call history in rredis"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper on method to store inputs and outputs"""
        key = method.__qualname__ + ":inputs"
        self._redis.rpush(key, str(args))
        data = method(self, *args, **kwargs)
        key_out = method.__qualname__ + ":outputs"
        self._redis.rpush(key_out, data)
        return data
    return wrapper


def replay(method: Callable) -> None:
    """Returns the history of calls made to a function"""
    name = method.__qualname__
    r = redis.Redis()
    key = method.__qualname__
    calls = r.get(key).decode("utf-8")
    print("Cache.store was called {} times:".format(calls))
    inputs = r.lrange(key + ":inputs", 0, -1)
    outputs = r.lrange(key + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("Cache.store(*{}) -> {}".format(i.decode('utf-8'),
                                              o.decode('utf-8')))


class Cache:
    """A cache class using redis instance"""
    def __init__(self) -> None:
        """ Initialise the class. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Stores an object in the redis instance using rand_key from uuid
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str, fn: Optional[Callable]) ->\
            Union[str, bytes, int, float]:
        """ Get method for the cache """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: bytes) -> str:
        """ Parametrize to string """
        return str((key).decode('utf-8'))

    def get_int(self, key: bytes) -> int:
        """ Parametrize to integer """
        try:
            data = str(key.decode('utf-8'))
            if not data.isdigit():
                raise ValueError('Not compatible')
            else:
                value = int(data)
        except Exception:
            value = 0
        return value
