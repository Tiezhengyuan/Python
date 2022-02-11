#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27,\n2020 9:13:24 AM$"

class test:
    def forStr(self,arr):
        for i in arr:
            print(i)

if __name__ == "__main__":
    a = list('abcde')
    test().forStr(a)
