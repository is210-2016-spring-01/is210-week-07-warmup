#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Using if and else statements"""


def bool_to_str(bval):
    """
    Args:
    bval(bool): Either true or false

    Return:
    str: Will return statement

    Example:
    >>> import task_02
    >>> task_02.bool_to_str(True)
    'Yes'

    >>> import task_02
    >>> task 02.bool_to_str('')
    'No'
    """
    if bval:
        print 'Yes'
    else:
        print 'No'
    result = 'Yes' or 'No'
    return result
