#!/usr/bin/python
# Author:   @BlankGodd_

from . import *
from datetime import datetime
import sys, time

class Load_bar:

    def __init__(self, name='Loading...', length=20, style='#', 
                    color=None):
        self.name = name
        bar = '[' + space(length) + "]"
        self.bar = [i for i in bar]
        self.style = style
        self.length = length
        self.start = datetime.utcnow()

    def iter(self, iterable):
        """Works in strings,lists,tuples and integers"""
        try:
            a = [i for i in iterable]
        except:
            a = [i for i in range(1,iterable+1)]
        length = len(a)
        x = self.getdiff(length)
        z = self.getdiff(length)
        count = 0
        y = 0
        for i in a:
            now = datetime.utcnow()
            yield i
            count += 1
            if count == x:
                y += 1
                if x * self.length == length:
                    self.bar[y] = self.style
                else:
                    if not third(y):
                        self.bar[y] = self.style
                x += z
            if i == a[-1]:
                for u in range(1,length+1):
                    self.bar[u] = self.style
            sys.stdout.flush()
            b = self.name + "".join(self.bar) + " || " + str(now-self.start)
            sys.stdout.write('\r' + b)
        print('\n')

    def getdiff(self,length):
        """Get difference between length of iteratot and length of bar"""
        if length < self.length:
            raise IterError("Iterable value too small")
        if length % self.length == 0:
            return length / self.length
        return length // self.length
