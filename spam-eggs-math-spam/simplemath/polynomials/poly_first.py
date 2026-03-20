#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
First-order polynomial evaluation.

This module provides a function for evaluating a first-order polynomial
(linear function) of the form:

.. math::

    f(x) = a_0 + a_1 x

Functions
---------
poly_first(x, a0, a1)
    Evaluate a first-order polynomial.

Dependencies
------------
No external dependencies.

Examples
--------
>>> from simplemath.polynomials.poly_first import poly_first
>>> poly_first(2, 1, 3)
7
>>> poly_first(0, 5, 10)
5
"""

def poly_first(x, a0, a1):
    """
    Evaluate a first-order polynomial.

    The polynomial has the form:

    .. math::

        f(x) = a_0 + a_1 x

    Parameters
    ----------
    x : int or float
        Value of the independent variable.
    a0 : int or float
        Zeroth-order coefficient (constant term).
    a1 : int or float
        First-order coefficient.

    Returns
    -------
    int or float
        The evaluated polynomial value.

    Examples
    --------
    >>> poly_first(3, 2, 4)
    14
    >>> poly_first(-1, 1, 5)
    -4
    """
    return a0 + a1 * x