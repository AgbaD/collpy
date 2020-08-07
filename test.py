#!/usr/bin/python
# Author:   @BlankGodd_

from colpy.loadbar import *
from colpy.unit import *

darkbar = Dark_bar()
loadbar = Load_bar()
squarebar = Square_bar()
circlebar = Circle_bar()

per = Percent(name='Processing...')

if __name__ == '__main__':
    
    print()
    loadbar.iter(1000000)
    darkbar.iter(1000000)
    squarebar.iter(1000000)
    circlebar.iter(1000000)

    print(2)

    per.iter(100)
