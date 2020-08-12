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

    def iter(self, iterable):
        """Works in strings,lists,tuples and integers"""
        self.start = datetime.utcnow()
        try:
            a = [i for i in iterable]
        except:
            a = [i for i in range(iterable)]
        length = len(a)
        x = self.getdiff(length)
        z = self.getdiff(length)
        count = 0
        y = 1
        for i in a:
            # yield i
            # increment count to know the number of items taken
            # from the list a
            count += 1
            if count == x:
                # if position isn't last
                if y != self.length:
                    self.bar[y] = self.style
                    y += 1
                x += z
            sys.stdout.flush()
            now = datetime.utcnow()
            b = self.name + "".join(self.bar) + " || " + str(now-self.start)
            sys.stdout.write('\r' + b)
            yield i
        # to make the load bar complete
        for u in range(1,self.length+1):
            self.bar[u] = self.style
        sys.stdout.flush()
        now = datetime.utcnow()
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

class Dark_bar(Load_bar):

    def __init__(self, name='Loading...', length=20, 
                    color=None):
        self.name = name
        bar = '[' + dot(length) + "]"
        self.bar = [i for i in bar]
        self.style = '█'
        self.length = length
        self.start = datetime.utcnow()

class Square_bar(Load_bar):

    def __init__(self, name='Loading...', length=20, 
                    color=None):
        self.name = name
        bar = '[' + square(length) + "]"
        self.bar = [i for i in bar]
        self.style = '▣'
        self.length = length
        self.start = datetime.utcnow()

class Circle_bar(Load_bar):

    def __init__(self, name='Loading...', length=20, 
                    color=None):
        self.name = name
        bar = '[' + circle(length) + "]"
        self.bar = [i for i in bar]
        self.style = '◉'
        self.length = length
        self.start = datetime.utcnow()

bars = {
    'darkbar': Dark_bar(),
    'loadbar': Load_bar(),
    'squarebar': Square_bar(),
    'circlebar': Circle_bar()
}