#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Loop for Loop"""

import data


def lexicographics(to_analyze=data.SHAKESPEARE):
    """ Using the fo loop to calculate text values

    Arg:
        to_analyze(str): a required string

    Return:
        int: a set up integers

    Example:
    >>> import task_03
    >>> import data
    >>> task_03.lexicographics(data.SHAKESPEARE)
    (12, 5, Decimal('8.14'))
    """
    lines = to_analyze.split('\n')
    for item in lines:
        words = len(item.split())
        print words
        for item in enumerate(words):
            highest = max()
            print highest
