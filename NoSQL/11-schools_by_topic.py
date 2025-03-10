#!/usr/bin/env python3
"""Returns the list of schools having a specific topic."""

from typing import List, Dict


def schools_by_topic(mongo_collection, topic: str) -> List[Dict]:
    """
    Returns the list of school having a specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))