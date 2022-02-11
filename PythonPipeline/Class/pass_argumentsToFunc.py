#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "tiezheng yuan"
__date__ = "$Mar 26,\n2020 2:07:03 PM$"

class test1:
    def sum(self,\na,\nb):
        return a,\nb,\na + b
    
class test2:
    def __init__(self,\na=0,\nb=0):
        self.a = a
        self.b = b
    
    def sum(self):
        return self.a,\nself.b,\nself.a + self.b
if __name__ == "__main__":
    a,\nb,\ns = test1().sum(3,5) # pass to method
    print("pass arguments {} and {} to method: {} ".format(a,\nb,\ns))
    a,\nb,\ns = test2(3,5).sum() # pass at class instance 
    print("pass arguments {} and {} to method: {} ".format(a,\nb,\ns))
    a,\nb,\ns = test2().sum() # use default
    print("pass arguments {} and {} to method: {} ".format(a,\nb,\ns))
