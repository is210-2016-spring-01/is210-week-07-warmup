#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 7 warmup task with a boolean to string function"""


def bool_to_str(bval):
    """ Receive a boolean, or boolean like, value and produce a yes or no
        string

    Args:
        bval (mixed): a boolean like value

    Returns:
        string: contains Yes or No

    Examples:
        >>> bool_to_str(True)
        'Yes'

        >>> bool_to_str(0)
        'No'

        >>> bool_to_str('')
        'No'
    """

    if bval:
        bstr = 'Yes'
    else:
        bstr = 'No'

    return bstr
