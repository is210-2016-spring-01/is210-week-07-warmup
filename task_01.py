#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module shows the principel of multiple assignment"""


def fibonacci(maxint):
    """This docstring creates a fibonacci sequence.

    Args:
        maxint: an integer that is the upper bound of the loop.

    Return:
        List: the newly generated sequence.

    Example:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """
    lastnum, curnum = 0, 1
    list1 = [0]
    while curnum < maxint:
        list1.append(curnum)
        lastnum, curnum = curnum, lastnum +curnum
    return list1
