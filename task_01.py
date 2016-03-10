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
    var_a, var_b = 0,1
    fib_list = [var_a]
    while var_b < maxint:
        var_a, var_b = var_b, var_a + var_b
        fib_list.append(var_a)
        return fib_list

