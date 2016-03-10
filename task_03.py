#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring is a for loop to count strings"""


import decimal as dec

def lexicographics(to_analyze):


    """ A function that calculates the maximun, minimum and average.

    Args:
        to_analyze(mixed): list of strings.

    Examples:
    import task_03
    >>> lexicographics('''Don't sto believing, Hold on to that feeling.''')
    (5, 3, Decimal(4.0))

    >>>import task_03
    >>>import data
    task_03.lexicographs(data.SHAKESPEARE)
    (12, 5, DECIMAL('8.14'))
    """
    mylist = []
    lines = to_analyze.split("\n")
    for line in lines:
        num_words = line.split()
        mylist.append(len(num_words))
    mymin = min(mylist)
    mymax = max(myList)
    myav = Decimal(sum(mylist))/Decimal(len(mylist))
    return mymax, mumin, myav
