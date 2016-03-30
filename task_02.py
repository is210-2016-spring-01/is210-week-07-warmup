#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docsting."""


def bool_to_str(bval):
    """Using if statements.

    Args:
        bval(str): Arguments to be tested its truthy or falsy values.

    Returns:
        var1: Returns the truthy or falsy values.

    Examples:

    >>> import task_02
    >>> task_02.bool_to_str(True)
    'Yes'
    >>> import task_02
    >>> task 02.bool_to_str('')
    'No'
    """
    if bval:
        var1 = 'Yes'
    else:
        var1 = 'No'
    return var1
