#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subtraction utility.

This module provides a single function, ``simple_sub()``, for subtracting
one value from another.

Functions
---------
simple_sub(a, b)
    Return the difference of ``a`` and ``b``.

Dependencies
------------
No external dependencies.

Examples
--------
>>> from simplemath.arithmetic.simple_sub import simple_sub
>>> simple_sub(10, 3)
7
>>> simple_sub(5.5, 2.0)
3.5
"""

def simple_sub(a, b):
    """
    Return the difference of ``a`` and ``b``.

    Parameters
    ----------
    a : int or float
        Value from which to subtract.
    b : int or float
        Value to subtract.

    Returns
    -------
    int or float
        The result of ``a - b``.

    Examples
    --------
    >>> simple_sub(8, 2)
    6
    >>> simple_sub(2.5, 0.5)
    2.0
    """
    return a - b