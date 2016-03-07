#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lexicographical analysis."""

import decimal


def lexicographics(to_analyze):
    """Looping for min/max/avg.

    Args:
        to_analyze (string): Required.

    Returns:
        tuple: Max, min and avg words/line.

    Examples:
        >>> import data
    >>> lexicographics(data.SHAKESPEARE)
    (12, 5, Decimal('8.14'))
    >>> lexicographics('Feelings\nNothing more than\nFeelings')
    (3, 1, Decimal('1.666666666666666666666666667'))
    """
    to_analyze = to_analyze.split('\n')
    wordct = []
    for number, line in enumerate(to_analyze):
        wordct.append(len(line.split()))
    return max(wordct), min(wordct), decimal.Decimal(sum(wordct)) / (number + 1)
