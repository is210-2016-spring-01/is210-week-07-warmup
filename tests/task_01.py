#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fib Sequence"""


def fibonacci(maxint):
    """this function performs and prints fibonacci sequence. It also shows how
    to use the while loop.

    Args:
        maxint (int): Ceiling Number (last number in the sequence)

    Returns:
        The entire fibonacci number up to the ceiling number

    Example:
        >>> task_01.fibonacci(20)
        [1, 1, 2, 3, 5, 8, 13] 3)

    """

    mylist = [0]
    lastnum, curnum = 0, 1
    while curnum < maxint:
        mylist.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return mylist
