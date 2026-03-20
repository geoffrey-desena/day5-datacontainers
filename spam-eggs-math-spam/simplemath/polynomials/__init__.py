# -*- coding: utf-8 -*-

"""
Polynomials subpackage
======================

This subpackage contains functions for evaluating low-order polynomials.

Modules
-------
poly_first
    Evaluate a first-order polynomial.

poly_second
    Evaluate a second-order polynomial.

Examples
--------
>>> from simplemath.polynomials import poly_first, poly_second
>>> poly_first(2, 1, 3)
7
>>> poly_second(2, 1, 3, 4)
23

Dependencies
------------
No external dependencies.
"""

from .poly_first import poly_first
from .poly_second import poly_second

__all__ = ["poly_first", "poly_second"]