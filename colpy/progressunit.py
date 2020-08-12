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
        print(self.name)
        try:
            a = [i for i in iterable]
        except:
            a = [i for i in range(iterable)]
        length = len(a)
        for i in a:
            k = (i/iterable) * 100
            k = round(k, 0)
            sys.stdout.write(u"\u001b[1000D" + str(k) + "%")
            time.sleep(0.001)
            sys.stdout.flush()
        print('\n')

class Spinner(Percent):
    phases = ('-', '\\', '|', '/','\\','|','-')
    
    def iter(self, iterable):
        if iterable < 2:
            raise IterError("Iterator value too small")
        print(self.name)
        ind = 0
        for i in self.gen(iterable + 1):
            if ind > 6:
                ind = 0
            k = self.phases[ind]
            ind += 1
            sys.stdout.write(u"\u001b[1000D" + str(k))
            time.sleep(0.1)
            sys.stdout.flush()
        print('\n')

        
