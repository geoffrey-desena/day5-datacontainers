#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arithmetic subpackage
=====================

This subpackage contains functions for basic arithmetic operations.

Modules
-------
simple_add
    Addition of two values.

simple_sub
    Subtraction of two values.

simple_mult
    Multiplication of two values.

simple_div
    Division of two values.

Examples
--------
>>> from simplemath.arithmetic import simple_add, simple_div
>>> simple_add(4, 5)
9
>>> simple_div(10, 2)
5.0

Dependencies
------------
No external dependencies.
"""

from .simple_add import simple_add
from .simple_sub import simple_sub
from .simple_mult import simple_mult
from .simple_div import simple_div

__all__ = ["simple_add", "simple_sub", "simple_mult", "simple_div"]