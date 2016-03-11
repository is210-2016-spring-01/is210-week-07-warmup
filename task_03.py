#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 3 file."""

import decimal
import data


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
    to_analyze = to_analyze.split('\n')
    word_count = len(to_analyze)
    count = 0
    for word in to_analyze:
        return min(to_analyze), max(to_analyze), decimal.Decimal(
            sum((to_analyze/count+1)))
