#!use/bin/env python
# -*- coding: utf-8 -*-
"""Week Seven  Warmup Loops."""


def bool_to_str(bval):
    """Evaluate the value of the function as True or False.

    Args:
        bvl (bool): boolean argument value to be evaluated.

    Returns:
        String: "Yes" if True or "No" if False.

    Examples:

        >>> bool_to_str('')
        'No'        
    """
    if bval == True:
        return "Yes"
    else:
        return "No"
