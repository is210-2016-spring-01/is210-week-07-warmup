#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 3 file."""

import decimal


def lexicographics(to_analyze):
    """to calculate the minimium, maxium, and the average words in the list.

    Args:
    to_analyze(list): a list.

    Returns:
    mixed: returns the min, max, and the average words in the lines.

    Examples:

        >>> lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        '(5, 3, Decimal(4.0))'
    """
    words = []

    for value in to_analyze.split('\n'):
        words.append(len(value.split()))
    return (max(words), min(words), decimal.Decimal(sum(words)/
            decimal.Decimal(len(words))))
