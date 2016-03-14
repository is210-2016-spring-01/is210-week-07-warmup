#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci Sequence"""


def fibonacci(maxint):
    """Creates a fibonacci sequence.

    Args:
        maxint = int which is upper bound of loop

    Returns:
        list = contains newly generated sequence

    Examples:
        >>> import task_01
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

    """"
    first, last = 0, 1
    while last < maxint:
        print last
        first, last = last, first+last
    return [result]
