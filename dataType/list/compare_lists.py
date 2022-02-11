#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27, 2020 6:40:39 PM$"

class test:
    def compList(self, arr1, arr2):
        a = set(arr1)
        b = set(arr2)
        print("A and B:", list(a & b))
        print("A or B without duplicats:", list(a | b))
        print("not(A and B):", list(a ^ b))
        print("only A:", list(a ^ a&b))
        print("only B:", list(b ^ a&b))
        
if __name__ == "__main__":
    a = [1,4,6,7]
    b = [4,6,8,10,
    3]
    test().compList(a, b)
