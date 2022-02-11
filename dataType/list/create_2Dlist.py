#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27, 2020 6:19:09 PM$"

class test:
    def test(self, nrow, ncol):
        arr = [[0]*ncol]
        for x in range(1, nrow):
            arr1 = [0]
            add = range(x, x*ncol, x)
            arr1.extend(add)
            arr.append(arr1)
        return arr
                
if __name__ == "__main__":
    a = test().test(4, 5)
    print(a)
