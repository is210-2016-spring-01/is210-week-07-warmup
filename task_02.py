#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module lets us practice the if statement"""


def bool_to_str(bval):
    """Yields a 'Yes' or 'No' statement wether or not input is true.

    Args:
        bval (bool): something truthy/falsey

    Returns:
        myvar (str): a string that says 'Yes' or 'No'.

    Example:
        >>> import task_02
        >>> task_02.bool_to_str(True)
        'Yes'
        >>> task_02.bool_to_str(' ')
        'No'
    """

    if bval:
        myvar = 'Yes'
    else:
        myvar = 'No'
    return myvar
