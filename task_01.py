#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""While loop to demonstrate multiple assignment."""


def fibonacci(maxint):
    """A function to use a while loop for multiple assignment.

    Args:
        maxint (int), required: Upper bounce parameter.

    Returns:
        list: Sum of elements defines next element in list.

    Examples:
        >>>fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

        >>>fibonacci(16)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    var_a, var_b = 0, 1
    fib_list = [var_a]
    while var_b < maxint:
        var_a, var_b = var_b, var_a + var_b
        fib_list.append(var_a)
    return fib_list
