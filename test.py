#!/usr/bin/python
# Author:   @BlankGodd_

from colpy.loadbar import *
from colpy.unit import *
from colpy.progbar import *

"""
darkbar = Dark_bar()
loadbar = Load_bar()
squarebar = Square_bar()
circlebar = Circle_bar()


per = Percent(name='Processing...')
spi = Spinner(name='Processing...')
"""

prog = Load_bar()

if __name__ == '__main__':
    for i in prog.iter('sade'):
        v = 1
        for j in range(10000000):
            v *= j
    
    """ 
    print()
    for i in loadbar.iter(1000000):
        print(27)
    darkbar.iter(1000000)
    squarebar.iter(1000000)
    circlebar.iter(1000000)

    print(2)

    per.iter(1000)
    spi.iter(1000)
    """

