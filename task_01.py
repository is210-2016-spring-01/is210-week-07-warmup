#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 1 docstring."""


def fibonacci(maxint):
    """Returns the fibonacci sequence.

    Args:
        maxint(int): Upper bound of the loop

    Returns:
        D(int): List of the fibonacci sequence

    Examples:

        >>> import task_01
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
        >>> import task_01
        >>> task_01.fibonacci(25)
        [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    listnum = [0]
    lastnum, curnum = 0, 1
    while curnum < maxint:
        listnum.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return listnum
