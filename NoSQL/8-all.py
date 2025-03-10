#!/usr/bin/env python3
""" Lists all the documents in a MongoDB collection."""

import pymongo


def list_all(mongo_collection):
    """
    Lists all the documents in a collection.
    """

    return [] if mongo_collection is None else mongo_collection.find()