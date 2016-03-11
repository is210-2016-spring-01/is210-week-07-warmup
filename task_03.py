#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring is a for loop to count strings"""


import decimal as dec

def lexicographics(to_analyze):


    """ A function that calculates the maximun, minimum and average.

    Args:
        to_analyze(mixed): list of strings.

    Examples:
       >>> lexicographics(data.SHAKESPEARE)
       (12, 5, Decimal('8.14'))
    """
    mylist = []
    lines = to_analyze.split("\n")
    for line in lines:
        num_words = line.split()
        mylist.append(len(num_words))
    mymin = min(mylist)
    mymax = max(mylist)
    myav = float(sum(mylist))/float(len(mylist))
    return mymax, mymin, myav
