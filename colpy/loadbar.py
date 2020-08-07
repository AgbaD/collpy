#!/usr/bin/python
# Author:   @BlankGodd_

from . import *
from datetime import datetime
import sys, time

class Load_bar:

    def __init__(self, name='Loading...', length=20, style='#', 
                    color=None):
        bar = '[' + space(length) + "]"
        self.bar = [i for i in bar] 
        self.start = datetime.utcnow()
        self.interval = 0
        self.length = length
        self.style = style
        self.count = 1
        self.name = name

    def next(self,x,i):
        count = 1
        if self.count <= self.length:
            if x * self.length == self.iterator:
                self.bar[self.count] = self.style
                self.count += 1
            else:
                if not third(count):
                    self.bar[self.count] = self.style
                    self.count += 1
                count += 1
                if i == (self.iterator-1):
                    for i in range(1,(length+1)):
                        self.bar[i] = self.style
        
    def get_diff(self,x):
        if x < 2:
            raise IterError("Iterator value too small")

        if x % self.length == 0:
            return x / self.length
        return x // self.length

    def iter(self, iterator):
        self.iterator = iterator
        x = self.get_diff(iterator)
        for i in range(iterator+1):
            now = datetime.utcnow()
            if i % x == 0:
                self.next(x,i)
                b = self.name + ''.join(self.bar) + str(now-self.start)
                sys.stdout.write('\r' + b)
                if iterator < 10000000:
                    time.sleep(0.1)
                sys.stdout.flush()
        

class Dark_bar(Load_bar):
    def __init__(self, name='Loading...', length=20, color=None):
        bar = '[' + dot(length) + "]"
        self.bar = [i for i in bar] 
        self.start = datetime.utcnow()
        self.interval = 0
        self.length = length
        self.style = '█'
        self.count = 1
        self.name = name


class Square_bar(Load_bar):
    def __init__(self, name='Loading...', length=20, color=None):
        bar = '[' + square(length) + "]"
        self.bar = [i for i in bar] 
        self.start = datetime.utcnow()
        self.interval = 0
        self.length = length
        self.style = '▣'
        self.count = 1
        self.name = name

class Circle_bar(Load_bar):
    def __init__(self, name='Loading...', length=20, color=None):
        bar = '[' + circle(length) + "]"
        self.bar = [i for i in bar] 
        self.start = datetime.utcnow()
        self.interval = 0
        self.length = length
        self.style = '◉'
        self.count = 1
        self.name = name
    