#!/usr/bin/python
# Author:   @BlankGodd_

from base import *
from datetime import datetime
import sys, time
import random


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
        start = datetime.utcnow()
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
            b = self.name + "".join(self.bar) + " || " + str(now-start)
            sys.stdout.write('\r' + b)
            yield i
        # to make the load bar complete
        for u in range(1,self.length+1):
            self.bar[u] = self.style
        sys.stdout.flush()
        now = datetime.utcnow()
        b = self.name + "".join(self.bar) + " || " + str(now-start)
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

class Percent:
    
    def __init__(self, name='Loading...'):
        self.name = name

    def iter(self, iterable):
        if iterable < 2:
            raise IterError("Iterator value too small")
        try:
            a = [i for i in iterable]
        except:
            a = [i for i in range(iterable)]
        length = len(a)
        ind = 1
        for i in a:
            val = None
            if ind <= length:
                k = (ind/length) * 100
                k = round(k, 0)
                val = self.name + " " + str(k) + "%"
            ind += 1
            sys.stdout.write('\r' + val)
            yield(i)
            sys.stdout.flush()
        print('\n')

class Spinner(Percent):
    phases = ('-', '\\', '|', '/','\\','|','-')
    
    def iter(self, iterable):
        start = datetime.utcnow()
        if iterable < 2:
            raise IterError("Iterator value too small")
        try:
            a = [i for i in iterable]
        except:
            a = [i for i in range(iterable)]
        length = len(a)
        ind = 0
        for i in a:
            if ind > 6:
                ind = 0
            k = self.phases[ind]
            now = datetime.utcnow()
            val = self.name + " " + str(k) + " " + str(now-start)
            ind += 1
            sys.stdout.write('\r' + val)
            yield(i)
            sys.stdout.flush()
        print("\n{} complete!".format(self.name))
        print('\n')

class Random_bar:

    def __init__(self, name='Loading...'):
        self.name = name
        self.style = '█'

    def make_bar(self):
        bar = '[' + space(20) + "]"
        self.bar = [i for i in bar]
    
    def iter(self, iterable):
        start = datetime.utcnow()
        if iterable < 2:
            raise IterError("Iterator value too small")
        try:
            a = [i for i in iterable]
        except:
            a = [i for i in range(iterable)]
        ind = [1, 3, 7, 11, 17, 20]
        for i in a:
            x = random.choice(ind)
            self.make_bar()
            for i in range(1, x+1):
                self.bar[i] = self.style
            sys.stdout.flush()
            now = datetime.utcnow()
            val = self.name + "".join(self.bar) + " || " + str(now-start)
            sys.stdout.write('\r' + val)
            yield(i)
        for i in range(1, 21):
            self.bar[i] = self.style
        sys.stdout.flush()
        now = datetime.utcnow()
        val = self.name + "".join(self.bar) + " || " + str(now-start)
        sys.stdout.write('\r' + val)
        print('\n')


bars = {
    'darkbar': Dark_bar(),
    'loadbar': Load_bar(),
    'squarebar': Square_bar(),
    'circlebar': Circle_bar(),
    'randombar': Random_bar(),
    'spinner': Spinner(),
    'percent': Percent()
}