#!/usr/bin/python
# Author:   @BlankGodd_

from . import space
try:
    from time import monotonic
except:
    from time import time as monotonic

class IterError(Exception):
    pass

class Load_bar:

	def __init__(self, name='Loading...', length=20, style='#', color=color_config):
        self.base = '['+space(length)+']'
        self.start = monotonic()
        self.interval = 0
        self.length = length

    def next(self):
        pass
        
    def get_diff(self, x):
        if x < 2:
            raise IterError("Iterator value too small")
        return x / self.length

    def iter(self, iterator):
        with self:
            for i in iterator:
                yield i
                self.get_diff(x)
        
        

