#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"Task 1 file."""


def fibonacci(maxint):
    """to add numbers to a list.

    Args:
    maxint(int): maxium number.

    Returns:
    list: returns a list with numbers.

    Examples:

        >>> fibonacci(10)
        '[0, 1, 1, 2, 3, 5, 8]'

        >>> fibonacci(22)
        '[0, 1, 1, 2, 3, 5, 8, 13, 21]'
    """
    as_a, as_b = 0, 1
    new_list = [as_a]

    while as_b < maxint:
        as_a, as_b = as_b, as_a + as_b
        new_list.append(as_a)
    return new_list
