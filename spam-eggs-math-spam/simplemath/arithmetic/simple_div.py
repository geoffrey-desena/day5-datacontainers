#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Division utility.

This module provides a single function, ``simple_div()``, for dividing one
value by another.

Functions
---------
simple_div(a, b)
    Return the quotient of ``a`` and ``b``.

Dependencies
------------
No external dependencies.

Examples
--------
>>> from simplemath.arithmetic.simple_div import simple_div
>>> simple_div(8, 2)
4.0
>>> simple_div(7, 2)
3.5
"""

def simple_div(a, b):
    """
    Return the quotient of ``a`` and ``b``.

    Parameters
    ----------
    a : int or float
        Numerator.
    b : int or float
        Denominator.

    Returns
    -------
    float
        The result of ``a / b``.

    Raises
    ------
    ZeroDivisionError
        If ``b`` is zero.

    Examples
    --------
    >>> simple_div(9, 3)
    3.0
    >>> simple_div(5, 2)
    2.5
    """
    return a / b