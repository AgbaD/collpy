# colpy
Add color highlights, load bars, progress displays and style to your python scripts and shell sessions

[Colpy Gist](https://gist.github.com/BlankGodd/9457548d94925de245f9a9bbcc1c3f02)

## Applications
- Highlight 
  - special texts
  - errors
        
- Create
  - Custom buttons
  - List bullet styles

- Progress bars
  - Multi-styled loading bars
  - Percentage progress display
  - Spinner progress display
  - Random load bar
  - Download bar 

## Usage
To use, install package using pip
```
$ pip3 install colpy
```
### Using Progress bars
Progress bars are used to tell how far or how long a process has gone or taken and 
how much is left to be done

It highlighs the lenght of the total procress and the time take to complete

Progress bars are best used when a user wants to iterate over a number of values
and perform actions on those values while taken note of the average time elapsed and
getting an idea of the time left for a process to reach completion.

Import package into python script or shell environment
```py
from colpy import *
# or single imports
from colpy import Load_bar

# Using a custom load bar

# The lenght indicates the size of the fullbar or the number of
# single bars  
loadbar = Load_bar(name="Processing...", length=20, style='$')
"""
The load bar can be loaded with the parameters absents
This makes the Load_bar use its default values
name = Loading...
length = 20
style = #

i.e
"""
loadbar = Load_bar()

# to iterate over an iterable, it is best if its length
# is a multiple of the the length of the bar
# For instance if we have a list of 30 items
# we could do
loadbar = Load_bar(length=10) # or 15 as the case may be

# to iterate over the list
# say

lst = [i for i in <whatever>]
# or 
string = 'some long string to be worked on'
# or 
val = 100

# we do
for i in loadbar.iter(lst): # or string or val
    # do some work on i

```

The same method applies for the following
But here, the styles are fixed and can't be changed
```py
darkbar = Dark_bar()
circlebar = Circle_bar()
squarenar = Square_bar()
```

### Using the random bar
```py
randombar = Random_bar()
# the name paramenter can be changed or left as default
randombar = Random_bar(name='Downloading... ')

# to use, call the iter method with the iterable
for i in random.iter(val):
    do som work on (i)
```

### Using the Spinner and percent
```py
spinner = Spinner()
# the name paramenter can be changed or left as default
spinner = Spinner(name='Authenticating... ')

# to use, call the iter method with the iterable
# support for a next() method will be available in future versions
for i in spinner.iter(val):
    do som work on (i)

# the same process works for percent
percent = Percent()
```

#### Support for a next() method for progress bars will 
#### be available in future versions

### Adding Highlights

