#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Statement to show truthiness."""


def bool_to_str(bval):
"""A function that returns yes/no string.

    Args:
        bval(bool), required: Truthy of Falsy.

    Returns:
        result: Yes or no string based on the bool value.

    Example:
    >>> bool_to_str(True)
    'Yes'

    >>> bool_to_str('')
    'No'
        """
    if bval:
        result = 'Yes'
    else:
        result = 'No'

    return result
