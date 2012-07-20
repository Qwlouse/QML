#!/usr/bin/python
# encoding: utf-8
from __future__ import division, print_function, unicode_literals
import functools
import numpy as np

def _e(entry, scope):
    return np.array(scope[entry] if entry in scope else float(entry))

def _v(line, scope):
    """
    Create a 1D numpy array from matlab-like-syntax string. For example:
    >>> v("1 2 3")
    array([ 1.,  2.,  3.])
    """
    return np.hstack(_e(entry, scope) for entry in line.strip().split())

def _m(matrix_string, scope):
    """
    Create a 2D numpy array from matlab-like-syntax string. For example:
    >>> m("1 2 3; 6 5 4; 7 8 9")
    array([[ 1.,  2.,  3.],
           [ 6.,  5.,  4.],
           [ 7.,  8.,  9.]])
    """ 
    return np.vstack(_v(row, scope) for row in matrix_string.split(';'))

empty_scope = dict()

e = functools.partial(_e, scope=empty_scope)
e.__doc__ = _e.__doc__

v = functools.partial(_v, scope=empty_scope)
v.__doc__ = _v.__doc__

m = functools.partial(_m, scope=empty_scope)
m.__doc__ = _m.__doc__

def set_scope(scope):
    e.keywords['scope'] = scope
    v.keywords['scope'] = scope
    m.keywords['scope'] = scope
