#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27, 2020 3:27:24 PM$"

class test:
    def __init__(self, arr):
        self.arr = arr
        self.len = len(arr)
        
    def listToList2(self, nrow=2):
        arr2 = []
        ncol = int(self.len/nrow)
        for i in range(ncol):
            s = self.arr[(0+i*nrow):(nrow+i*nrow)]
            arr2.append(s)
            #print(s)
        return arr2
    
    def list2ToList(self):
        arr2 = [j for row in self.arr for j in row]
        return arr2
        
if __name__ == "__main__":
    a = list(range(12));   print(a)
    print(test(a).listToList2(3))
    b = test(a).listToList2(2);    print(b)
    print(test(b).list2ToList())
