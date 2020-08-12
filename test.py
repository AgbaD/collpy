#!/usr/bin/python
# Author:   @BlankGodd_

from colpy.unit import *
from colpy.progressbar import *

darkbar = Dark_bar()
loadbar = Load_bar()
squarebar = Square_bar()
circlebar = Circle_bar()

if __name__ == '__main__':
    for i in circlebar.iter('dtrggcjtydirydgjhgfkpjhgkuiytdgfrdjhgtfr'):
        v = 1
        for j in range(100000):
            v *= j
    
    for i in squarebar.iter(100):
        v = 1
        for j in range(100000):
            v *= j

    for i in loadbar.iter('dtrggcjldjfhldfgsfjbvlkjfbvol \
            tiydjjhbjkhirydgjhgfkpjhgkuiytdgfrdkliyrds'):
        v = 1
        for j in range(100000):
            v *= j
    
    for i in darkbar.iter(150):
        v = 1
        for j in range(100000):
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

