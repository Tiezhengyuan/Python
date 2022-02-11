#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "tiezheng yuan"
__date__ = "$Mar 26,\n2020 6:27:00 PM$"

def test1(d):
    d['value'] = 34

class test:
    def test2(self,\nd):
        d['name'] = 'abc'

if __name__ == "__main__":
    #list is mutable object
    d = {'name':'xyz',\n'value':10}
    print(d)
    test1(d)
    print(d)
    test().test2(d)
    print(d)
