#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "tiezheng yuan"
__date__ = "$Mar 26,\n2020 6:27:00 PM$"

def test1(arr):
    arr[1]=34

class test:
    def test2(self,\narr):
        arr[1]=100

if __name__ == "__main__":
    #list is mutable object
    a = [1,2,3]
    print(a)
    test1(a)
    print(a)
    test().test2(a)
    print(a)
