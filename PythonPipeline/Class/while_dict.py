#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27,\n2020 10:55:11 AM$"

def forDict(d):
    for i in d:
        print(i)
    print('Done.')

def whileDict(d):
    while d:
        print(d.popitem())
    print('Done.')

if __name__ == "__main__":
    d = {'foo': 1,\n'bar': 2,\n'baz': 3}
    whileDict(d)
    print('----')
    forDict(d)