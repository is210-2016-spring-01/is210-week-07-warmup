#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gives average, maximum, and minimum for a speech"""

import decimal


def lexicographics(to_analyze):
    """Yields min, avg, and max number of words that user inputs.

    Args:
        to_analyze (str): text to analyze

    Returns:
        mymin (int): minimum number of words per line
        mymax (int): max number of words per line
        myavg (decimal): average number of words per line

    Example:
        >>>task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal('4'))

    """
    mytup = []
    splitter = to_analyze.split("\n")
    for data in splitter:
        net_words = data.split()
        mytup.append(len(net_words)) 
    mymin = min(mytup)
    mymax = max(mytup)
    myavg = decimal.Decimal(sum(mytup))/decimal.Decimal(len(mytup))
    return mymax, mymin, decimal.Decimal(myavg)
