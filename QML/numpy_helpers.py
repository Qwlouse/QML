#!/usr/bin/python
# encoding: utf-8
from __future__ import division, print_function, unicode_literals
import numpy as np

def v(s):
    """
    Create a 1D numpy array from matlab-like-syntax string. For example:
    >>> v("1 2 3")
    array([ 1.,  2.,  3.])
    """
    return np.array(float(e) for e in s.strip().split())

def m(s):
    """
    Create a 2D numpy array from matlab-like-syntax string. For example:
    >>> m("1 2 3; 6 5 4; 7 8 9")
    array([[ 1.,  2.,  3.],
           [ 6.,  5.,  4.],
           [ 7.,  8.,  9.]])
    """ 
    return np.array([v(r) for r in s.split(";")])


def main():
    pass

if __name__ == "__main__":
    main()
