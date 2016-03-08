#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""If and else statements to determine truthiness."""


def bool_to_str(bval):
    """A function to determine bool value and return Yes/No string.

    Args:
        bval (bool), required: Truthy or falsy value to evaluate.

    Returns:
        result: Yes or No string based on bool value.

    Examples:
        >>> bool_to_str(True)
        'Yes'

        >>> bool_to_str('')
        'No'
    """
    if bval is True:
        result = 'Yes'
    elif bval is not '':
        result = 'Yes'
    else:
        result = 'No'

    return result
