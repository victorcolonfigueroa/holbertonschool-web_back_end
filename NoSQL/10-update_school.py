#!/usr/bin/env python3
"""Changes all topics of a school document based on the name."""

import pymongo
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """
    Changes all topics of a school doc based on the name

    Args:
        name(str): will be the school name to update

        topics(List[str]): will be the list of topics
        approached in the school
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )