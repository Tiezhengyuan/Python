# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"

from itertools import permutations
class test:
    def __init__(self,str):
        self.str = str
    
    def permuStr(self):
        a = [''.join(p) for p in permutations(self.str)]
        return(a)
        
    def permuSent(self):
        arr = self.str.split(" ")
        a = [' '.join(p) for p in permutations(arr)]
        return(a)
        
        
if __name__ == "__main__":
    a = test("permute").permuStr()
    print(a)
    b = test("Here we go now").permuSent()
    print(b)
    
