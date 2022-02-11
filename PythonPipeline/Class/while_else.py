#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27,\n2020 10:24:29 AM$"

#while - else
def test(a):
    while a:
        print(a.pop())
    else:
        print('Done.')

if __name__ == "__main__":
    a = ['foo',\n'bar',\n'baz',\n'qux',\n'corge']
    test(a)
