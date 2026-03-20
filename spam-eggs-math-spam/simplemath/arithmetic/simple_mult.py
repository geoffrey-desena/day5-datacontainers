#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multiplication utility.

This module provides a single function, ``simple_mult()``, for multiplying
two values.

Functions
---------
simple_mult(a, b)
    Return the product of ``a`` and ``b``.

Dependencies
------------
No external dependencies.

Examples
--------
>>> from simplemath.arithmetic.simple_mult import simple_mult
>>> simple_mult(3, 4)
12
>>> simple_mult(2.5, 2)
5.0
"""

def simple_mult(a, b):
    """
    Return the product of ``a`` and ``b``.

    Parameters
    ----------
    a : int, float, or compatible type
        First factor.
    b : int, float, or compatible type
        Second factor.

    Returns
    -------
    int, float, or compatible type
        The result of ``a * b``.

    Notes
    -----
    Because Python's ``*`` operator is used, this function may also work
    with compatible non-numeric types, such as multiplying a string by an
    integer.

    Examples
    --------
    >>> simple_mult(6, 7)
    42
    >>> simple_mult(1.5, 4)
    6.0
    """
    return a * b