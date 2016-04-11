#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Functions with return statements"""


def bool_to_str(bval):
    """Tells you if something is true or false.

    Args:
        bval = bool. evaluated for truthiness or falsiness
    Returns:
        str = 'Yes' if True. 'No' if False.
    Examples:
        >>> import task_02
        >>> task_02.bool_to_str(True)
        'Yes'

        >>> import task_02
        >>> task 02.bool_to_str('')
        'No'

    """
    if bval is True:
        print 'Yes'
    else:
        print 'No'
    return bool_to_str
