#!/usr/bin/python
# Author:   @BlankGodd_

from colpy.progressunit import *

per = Percent()
spi = Spinner()

if __name__ == "__main__":
    for i in per.iter(100):
        a = [i*j for j in range(1000000)]

    for i in spi.iter(100):
        a = [i*j for j in range(1000000)]