#!/usr/bin/env python3

"""
Inserts a new document based on keyword args
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert using Keyword argsss.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
