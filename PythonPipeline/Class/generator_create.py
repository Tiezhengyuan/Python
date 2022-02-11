#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "tiezheng yuan"
__date__ = "$Mar 26,\n2020 8:23:20 AM$"

#normal function
def func_square(n):
    arr = []
    for i in range(n):
        arr.append(i**2)
    return arr
def generator_square(n):
    for i in range(n):
        yield i**2
if __name__ == "__main__":
    #generate list all at once
    print(func_square(10))
    #iterator
    g = generator_square(10)
    print(g) # generator is an object
    print(next(g)) # call back a value
    print(next(g))# call back another value
    print(next(g))# call back another value
    
    
