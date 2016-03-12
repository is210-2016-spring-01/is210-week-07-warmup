#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gives average, maximum, and minimum for a speech"""

import decimal


def lexicographics(to_analyze):

    mytup = []
    splitter = to_analyze.split("\n")
    for data in splitter:
        net_words = data.split()
        mytup.append(len(net_words)) 
    mymin = min(mytup)
    mymax = max(mytup)
    myavg = decimal.Decimal(sum(mytup))/decimal.Decimal(len(mytup))
    return mymax, mymin, decimal.Decimal(myavg)
