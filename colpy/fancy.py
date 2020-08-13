#!/usr/bin/python
# Author:   @BlankGodd_

base =  '\033[0m'
colors = {
    'red':1,
    'green':2,
    'orange':3,
    'blue':4,
    'purple':5,
    'lightblue':6,
    'cyan':7
}

class Botton:
	bottons = ['x','=','+','*','~','$','#','@',' ','-']
	out = ['[',']']

	def __init__(self, ind=0, outer=True, color='red'):
        bbase =  '\033[9{}m'
        style = self.bottons[ind]
        color = colors[color]
        val = ''
        if outer:
            val = '[' + bbase.format(str(color)) + style + base + ']'
        else:
            val = bbase.format(str(color)) + style + base
        return val

class
