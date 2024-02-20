#!/usr/bin/env python3
""" Helper function
"""

def index_range(page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index
