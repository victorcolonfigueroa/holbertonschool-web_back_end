#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""


import csv
import math
from typing import List, Tuple, Dict


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of data from the dataset
        based on the page number and page size.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding
            to the specified page and page size.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end] if start < len(data) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page
        next_page: number of the next page
        prev_page: number of the previous page
        total_pages: the total number of pages in the dataset as an integer

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing the page_size, page, data,
            next_page, prev_page, and total_pages.
        """
        current_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = (total_items + page_size - 1) // page_size
        return {
            'page_size': page_size,
            'page': page,
            'data': current_page,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
        }