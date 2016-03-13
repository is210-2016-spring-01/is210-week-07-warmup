#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 3 docstring."""


import decimal


def lexicographics(to_analyze):
    """Calculation of maximum, minimum, and average length of words in a speech.

    Args:
        to_analyze(str): Speech to be analyzed.

    Returns:
        varmax: Maximum number of words in  speech
        varmin: Minimum number of words in speech
        varavg: Average length of words in speech

    Examples:

        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal(4.0))
        >>> import task_03
        >>> import data
        >>> task_03.lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    var1 = []
    to_split = to_analyze.split("\n")
    for words in to_split:
        var1.append(len(words.split()))

    varmax = max(var1)
    varmin = min(var1)
    varavg = decimal.Decimal(sum(var1))/decimal.Decimal(len(var1))
    return varmax, varmin, varavg
