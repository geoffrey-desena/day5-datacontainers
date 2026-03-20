#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Addition utility.

This module provides a single function, ``simple_add()``, for adding two
numbers or other compatible Python objects.

Functions
---------
simple_add(a, b)
    Return the sum of ``a`` and ``b``.

Dependencies
------------
No external dependencies.

Examples
--------
>>> from simplemath.arithmetic.simple_add import simple_add
>>> simple_add(2, 3)
5
>>> simple_add(2.5, 1.5)
4.0
>>> simple_add("hello ", "world")
'hello world'
"""

def simple_add(a, b):
    """
    Return the sum of ``a`` and ``b``.

    Parameters
    ----------
    a : int, float, or compatible type
        First value to add.
    b : int, float, or compatible type
        Second value to add.

    Returns
    -------
    int, float, or compatible type
        The result of ``a + b``.

    Notes
    -----
    This function uses Python's ``+`` operator, so it also works with
    compatible non-numeric types such as strings and lists.

    Examples
    --------
    >>> simple_add(1, 2)
    3
    >>> simple_add(1.2, 3.4)
    4.6
    """
    return a + b