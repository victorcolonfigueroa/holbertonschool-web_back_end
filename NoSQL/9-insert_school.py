#!/usr/bin/env python3
"""Inserts a new document in a MongoDB collection."""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    """
    new_doc = mongo_collection.insert_one({**kwargs})
    return new_doc.inserted_id
