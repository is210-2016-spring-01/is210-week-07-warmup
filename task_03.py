#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 7 warmup task with a lexicographical analysis function"""

import decimal


def lexicographics(to_analyze):
    """ Receive a string and analyze the number of words per line (min, max,
        and mean)

    Args:
        to_analyze (string): a string of sentences deliniated by newline

    Returns:
        tuple: containing the (maximum, minimum, and average) number or words
               per line

    Examples:
        >>> lexicographics('''Mary had a little lamb,
        Its fleece was white as snow.
        and everywhere that Mary went
        the lamb was sure to go.'''
        (6, 5, Decimal(5.5))
    """

    line_max, line_min = 0, -1             # initialize counts
    tot_words, lines = 0, 0

    for lines, linewrds in enumerate(to_analyze.split('\n')):

        wcount = len(linewrds.split(' '))

        if line_min < 0:                    # if min not set, set now
            line_min = wcount
        elif wcount < line_min:             # otherwise check for lower count
            line_min = wcount

        if wcount > line_max:               # if new higher max, set count
            line_max = wcount

        tot_words += wcount                 # total number of words

    return (line_max, line_min, decimal.Decimal(tot_words) /
            decimal.Decimal(lines + 1.0))
