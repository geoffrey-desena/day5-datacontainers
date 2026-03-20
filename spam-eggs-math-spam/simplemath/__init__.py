#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simplemath
==========

A small educational package containing simple arithmetic operations and
polynomial evaluation utilities.

Subpackages
-----------
arithmetic
    Basic arithmetic functions such as addition, subtraction,
    multiplication, and division.

polynomials
    Polynomial evaluation functions.

Examples
--------
Import directly from the package:

>>> from simplemath import simple_add, poly_second
>>> simple_add(2, 3)
5
>>> poly_second(2, 1, 3, 4)
23

Dependencies
------------
This package has no external dependencies and uses only the Python
standard library.
"""

from .arithmetic import simple_add, simple_sub, simple_mult, simple_div
from .polynomials import poly_first, poly_second

__all__ = [
    "simple_add",
    "simple_sub",
    "simple_mult",
    "simple_div",
    "poly_first",
    "poly_second",
]
