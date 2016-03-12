#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a fibonacci sequence."""


def fibonacci(maxint):
    """ this function does the fibonacci sequence based on
    the user's maximum number.

    Args:
        maxint (int): how high the user wants the sequence to go

    Returns:
        A fibonacci sequence list that rises up to maxint.

    Examples:
        >>> import task_01
        >>> task_01.fibonacci(10
        
    """
    
    sequence = [0]
    lastnum, curnum = 0, 1
    while curnum < maxint:
        sequence.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return sequence
