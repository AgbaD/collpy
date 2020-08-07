#!/usr/bin/python
# Author:   @BlankGodd_

__version__ = '0.0.3'


def space(n):
        return " " * n

class IterError(Exception):
    pass

def third(x):
    return True if x % 3 == 0 else False
