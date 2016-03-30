#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""For loop to word counts of strings."""

import decimal as dec


def lexicographics(to_analyze):
    """A function to find the max, min, and average words in string(s).

    Args:
        to_analyze (mixed), required: Inputted string or list of strings.

    Returns:
        tuple: Includes max words, min words, and average words of strings.

    Examples:
        >>>lexicographics('''Don't stop believing,
            Hold on to that feeling.''')
        (5, 3, Decimal('4'))

        >>>task_03.lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    to_analyze = to_analyze.split('\n')
    total_statements = dec.Decimal(len(to_analyze))
    loop_count, word_count = 0, 0
    average_words = dec.Decimal(0.0)
    word_count_list = []
    for word_count in to_analyze:
        word_count = len(to_analyze[loop_count].split())  # Find current length
        word_count_list += [word_count]  # Build list of word counts
        loop_count += 1  # Increment loop count to increment index

    average_words = sum(word_count_list) / total_statements

    return (max(word_count_list), min(word_count_list), average_words)
