#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27,\n2020 9:13:24 AM$"

class test:
    def forDict(self,d):
        for key in d.keys():
            print(key,\nd[key])

if __name__ == "__main__":
    d = {'name':'smith',\n'age':34}
    test().forDict(d)
