#!/usr/bin/env python3

"""
Change School topics
"""


def update_topics(mongo_collection, name, topics):
    """Updates a particular school with name"""
    mongo_collection.update_many({ "name": name }, { "$set": { "topics": topics }})
