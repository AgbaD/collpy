#!/usr/bin/python
# Author:   @BlankGodd_

base =  '\033[0m'
colors = {
    'black':0,
    'red':1,
    'green':2,
    'orange':3,
    'blue':4,
    'purple':5,
    'lightblue':6,
    'cyan':7
}


def botton(ind=0, outer=True, color='red'):
    bottons = ['x','=','+','*','~','$','#','@',' ','-']
    out = ['[',']']
    bbase = '\033[9{}m'
    style = bottons[ind]
    color = colors[color]
    val = None
    if outer:
        val = '[' + bbase.format(str(color)) + style + base + '] ' 
    else:
        val = bbase.format(str(color)) + style + base + " "
    return val

def cprint(txt=None, color='green'):
    bbase = '\033[9{}m'
    color = colors[color]
    bbase = bbase.format(str(color))
    print(bbase + txt + base)

def highlight(txt=None, color='red'):
    bbase = '\033[4{}m'
    color = colors[color]
    bbase = bbase.format(str(color))
    val = bbase + txt + base
    return val



