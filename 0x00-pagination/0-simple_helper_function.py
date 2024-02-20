#!/usr/bin/env python3
""" Helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns tuple for start and end index.
    """
    return ((page - 1) * page_size, page * page_size)
