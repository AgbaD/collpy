#!/usr/bin/python
# Author:   @BlankGodd_

from colpy.progressbar import *

per = Percent()
spi = Spinner()
rand = Random_bar()

if __name__ == "__main__":
    """
    for i in per.iter(100):
        a = [i*j for j in range(1000000)]

    for i in spi.iter(100):
        a = [i*j for j in range(1000000)]
    """

    for i in rand.iter(200):
        a = [i*j for j in range(1000000)]