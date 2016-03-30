#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A fibonacci sequence generator."""


def fibonacci(maxint):
    """Fibonacci module.

    Args:
        maxint (int): Upper bound of loop.

    Returns:
        list: A fibonacci sequence.

    Examples:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
        >>> fibonacci(30)
        [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    lastnum, curnum = 0, 1
    list1 = [0]
    while curnum < maxint:
        list1.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return list1
