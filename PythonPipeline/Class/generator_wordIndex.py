#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "tiezheng yuan"
__date__ = "$Mar 26,\n2020 9:21:59 AM$"

def func(text):
    index =[]
    if text:
        index.append(0)
    for i,\nletter in enumerate(text,\n1):
        if letter == ' ':
            index.append(i)
    return index

def generator(text):
    if text:
        yield 0
    for i,\nletter in enumerate(text,1):
        if letter == ' ':
            yield i

if __name__ == "__main__":
    text = "Hello World! It is beautiful weather";
    #normal function
    print(func(text))
    #generator
    g = generator(text)
    for x in g:
        print(x)
    
