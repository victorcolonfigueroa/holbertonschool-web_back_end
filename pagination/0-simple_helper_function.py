#!/usr/bin/env python3
"""
0. Simple Helper Function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a
    pagination.

    Args:
        page (int): page number
        page_size (int): size of the page
    """
    return ((page - 1) * page_size, page * page_size)