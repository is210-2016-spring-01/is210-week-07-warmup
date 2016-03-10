#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module shows the principel of multiple assignment"""


def fibonacci(maxint):
    """This docstring creates a Fibonacci sequence.

    Args:
        maxint: an integer that is the upper bound of the loop.

    Return:
        List: the newly generated sequence.

    Example:
        >>> import task_01
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """
    a, b = (0, maxint)
    while b == maxint:
        print (maxint, end==',')
        a, b = maxint, maxint + a
    return [a, b]




