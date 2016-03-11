#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 2 file."""


def bool_to_str(bval):
    """To input a boolean value, and return a string.

    Args:
    bval(mixed): input a value.

    Returns:
    Str: returns yes or no, as a string.

    Examples:

        >>> bool_to_str(True)
        ''Yes''

        >>> bool_to_str(False)
        ''No''

        >>> bool_to_str('')
        ''No''
    """
    if bval:
        return 'Yes'
    else:
        return 'No'
