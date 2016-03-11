#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Understanding Fibonacci sequence"""


def fibonacci(maxint):
    """
    Args:
    maxint(int): An integer that will serve as the upper bount of the loop

    Return:
    int: All items are returned in int

    Example:
    >>> import task_01
    >>> task_01.fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8]
    """
    initial, maxint = 0, 1
    while maxint < 10:
        print [maxint]
        initial, maxint = maxint, initial + maxint
    return
