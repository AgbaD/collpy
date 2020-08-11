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
        if isinstance(iterable,(str,list,tuple)):
            it_len = len(iterable)
            k = (1/it_len) * 20
            for val in iterable:
                sys.stdout.flush()
                now = datetime.utcnow()
                yield val
                if val == iterable[-1]:
                    self.bar = [self.style] * self.length
                else:
                    u = 1
                    if u < it_len:
                        for i in range(u*(int(k)) +1):
                            self.bar[i] = self.style 
                        u += 1
                timee = now - self.start
                output = "" + self.name + "".join(self.bar) + ' || ' + str(timee) + ""
                sys.stdout.write(output)
                sys.stdout.flush()

