#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Second-order polynomial evaluation.

This module provides a function for evaluating a second-order polynomial
(quadratic function) of the form:

.. math::

    f(x) = a_0 + a_1 x + a_2 x^2

Functions
---------
poly_second(x, a0, a1, a2)
    Evaluate a second-order polynomial.

Dependencies
------------
This module depends on :func:`simplemath.polynomials.poly_first.poly_first`
to compute the constant and linear terms before adding the quadratic term.

Examples
--------
>>> from simplemath.polynomials.poly_second import poly_second
>>> poly_second(2, 1, 3, 4)
23
>>> poly_second(1, 0, 2, 1)
3
"""

from .poly_first import poly_first


def poly_second(x, a0, a1, a2):
    """
    Evaluate a second-order polynomial.

    The polynomial has the form:

    .. math::

        f(x) = a_0 + a_1 x + a_2 x^2

    This implementation reuses :func:`poly_first` to evaluate the constant
    and linear parts of the expression.

    Parameters
    ----------
    x : int or float
        Value of the independent variable.
    a0 : int or float
        Zeroth-order coefficient (constant term).
    a1 : int or float
        First-order coefficient.
    a2 : int or float
        Second-order coefficient.

    Returns
    -------
    int or float
        The evaluated polynomial value.

    See Also
    --------
    poly_first : Evaluate a first-order polynomial.

    Examples
    --------
    >>> poly_second(2, 1, 3, 4)
    23
    >>> poly_second(0, 5, 2, 7)
    5
    """
    return poly_first(x, a0, a1) + a2 * (x ** 2)