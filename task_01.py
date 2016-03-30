#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 7 warmup task with a fibonacci function"""


def fibonacci(maxint):
    """Produce a list of numbers following the Fibonacci sequence up to the
       specified maximum value

    Args:
        maxint (int): the upper limit of the Fibonacci number.

    Returns:
        list: contains the list of numbers produced by the sequence.

    Examples:
        >>> fibonacci(8)
        [0, 1, 1, 2, 3, 5]

        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

        >>> fibonacci(24)
        [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """

    first, second = 0, 1                 # initialize counters
    fibolist = [0]

    while second < maxint:

        fibolist.append(second)                   # add new number to list
        first, second = second, first + second    # save current and add first

    return fibolist
