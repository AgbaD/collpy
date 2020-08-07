#!/usr/bin/python
# Author:   @BlankGodd_

from colpy.loadbar import *

darkbar = Dark_bar()
loadbar = Load_bar()
squarebar = Square_bar()
circlebar = Circle_bar()

if __name__ == '__main__':
    loadbar.iter(iterator=10000000)
    darkbar.iter(iterator=10000000)
    squarebar.iter(iterator=10000000)
    circlebar.iter(iterator=10000000)
