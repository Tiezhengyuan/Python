#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "tiezheng yuan"
__date__ = "$Mar 26,\n2020 2:27:05 PM$"

def test(a,\n*pargs,\n**kargs):
    print(a,\npargs)
    print(kargs)

if __name__ == "__main__":
    test(1,2,3,\nx=1,\ny=2)
