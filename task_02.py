#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""If function to return yes or no."""


def bool_to_str(bval):
    """Determines if value to truthy or falsy.

    Args:
        bval (bool): Truthy or falsy value.

    Returns:
        string: Value of 'yes' or 'no'.

    Examples:
        >>> bool_to_str(False)
        'No'
        >>> bool_to_str(True)
        'Yes'
    """
    if bval:
        return 'Yes'
    else:
        return 'No'
