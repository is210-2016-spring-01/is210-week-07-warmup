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
    to_analyze = to_analyze.split('/n')
    average_words = dec.Decimal(0.0)
    word_count_list = []
    count = 0
    for word_count in (to_analyze):
        word_count_list.append(len(to_analyze).split())
        count = word_count
    return max(word_count_list), min(word_count_list), \
           decimal.Decimal(sum(word_coun_list)) / (count + 1)
