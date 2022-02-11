#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27,\n2020 9:13:24 AM$"

class test:
    def getSquare(self,n):
        for i in range(n):
            yield i**2
    def forGenerator(self):
        for n in self.getSquare(10):
            print(n)

if __name__ == "__main__":
    test().forGenerator()
