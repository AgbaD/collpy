#!/usr/bin/python
# Author:   @BlankGodd_

__version__ = '0.0.3'


def space(n):
        return " " * n

def dot(n):
        return "." * n

def square(n):
        return '▢' * n

def circle(n):
        return '◯' * n

def third(x):
    return True if x % 3 == 0 else False


class IterError(Exception):
    pass

