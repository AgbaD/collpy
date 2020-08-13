#!/usr/bin/python
# Author:   @BlankGodd_

import time, sys
from . import IterError


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
            val = self.name + " " + str(k)
            ind += 1
            sys.stdout.write('\r' + val)
            yield(i)
            sys.stdout.flush()
        print('\n')

        
