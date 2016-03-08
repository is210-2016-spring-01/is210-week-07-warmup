#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Word Count"""

from decimal import Decimal


def lexicographics(to_analyze):
    """Lexicographics returns max, min and average number of words
       in each entry.

    Args:
        to_analyze (mixed): Analysing Text

    Returns:
        max (int): maximum number of words in a sentence
        min (int): minimum number of words in a sentence
        average (decimal): average number of words in the text
    Example:
        >>> lexicographics('''This is a test, and only a test''')
        (8, 8, Decimal('8'))
    """
    mylist = []
    lines = to_analyze.split("\n")
    for line in lines:
        num_words = line.split()
        mylist.append(len(num_words))
    mymin = min(mylist)
    mymax = max(mylist)
    myav = Decimal(sum(mylist))/Decimal(len(mylist))
    return mymax, mymin, myav
