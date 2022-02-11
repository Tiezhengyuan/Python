#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "tiezheng yuan"
__date__ = "$Mar 27, 2020 3:18:10 PM$"

class test:
    #remove duplicated element
    def removeDup(self, arr):
        unique = set(arr)
        return list(unique)
        
if __name__ == "__main__":
    a = [ 1,2,3,4,5,3,5,0,23,4,26,87]
    print(a)
    print(test().removeDup(a))
