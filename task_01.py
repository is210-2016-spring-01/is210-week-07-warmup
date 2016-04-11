#!use/bin/env python
# -*- coding: utf-8 -*-
"""Week Seven  Warmup Loops."""


def fibonacci(maxint):
    """Does some math and returns a sequence.

    Args:
        maxint (int): Argument is an integer that will be used for calculation.

    Returns:
        Tuple: Fibonacci sequence.

    Examples:

        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

        >>> fibonacci(20)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    a, b = 0, 1
    res = [a]
    while b < maxint:
        res.append(b)
        a, b = b, b+a

    return res
