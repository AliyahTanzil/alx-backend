#!/usr/bin/env python3

"""
index_range function

This function takes two integer arguments, page and page_size,
and returns a tuple containing a start index and an end index
corresponding to the range of indexes to return in a list for
those particular pagination parameters.

Parameters:
    page (int): The page number for which the range needs to
      be calculated (1-indexed).
    page_size (int): The number of items per page.

Returns:
    tuple: A tuple containing the start index and end index
    of the range.

Example:
    >>> start, end = index_range(2, 10)
    >>> print(f"Start Index: {start}, End Index: {end}")
    Start Index: 10, End Index: 19

Note:
    - Page numbers and page sizes should be positive integers.
    - The function assumes 1-indexed pages, meaning the first
    page is page 1.
"""


def index_range(page, page_size):
    """
    Function to calculate the start and end index of the range
    of indexes to return in a list for those particular pagination
    parameters.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
