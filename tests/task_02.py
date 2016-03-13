#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Truth and nothing but the truth."""


def bool_to_str(bval):
    """This is a function that prints 'Yes' or 'No' pertaining to whether or 
    not a statement is true

    Args:
        bval (boolean): True or False

    Returns:
        'Yes' or 'No'

    Example:
        >>> bool_to_str(True)
        'Yes'

    """

    if bval:
        response = 'Yes'
    else:
        response = 'No'
    return response
