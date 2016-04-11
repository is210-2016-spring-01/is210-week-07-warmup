#!use/bin/env python
# -*- coding: utf-8 -*-
"""Week Seven  Warmup Loops."""

import decimal


def lexicographics(to_analyze):
    """Calculates the min, max and average length.

    Args:
        to_analyze (str): argument to calculate min, max and avrge for.

    Returns:
        Tuple (mixed): integers and decimal.

    Examples:

        >>>lexicographics('''Don't stop believeing, Hold on to that feeling.''')
        (5, 3, Decimal(4.0))
    """
    lines = to_analyze.split("\n ")
    min = 0
    max = 0
    sum = 0
    counter = 0.0
    for item in range(len(lines)):
        data = lines[item].split(" ")
        if len(data) > max:
            max = len(data)
        if len(data) < min:
            min = len(data)

        counter = counter + 1.0
        sum = sum + len(data)

    return (max, min, decimal.Decimal(sum)/decimal.Decimal(counter))
