# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"
class test:
    def __init__(self,str):
        self.str = str
    
    def reverse(self):
        return self.str[::-1]
    
    def complimentary(self):
        com = self.str.upper().replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
        return com
    
    def rev_comp(self):
        rev = self.reverse()
        rev_com = test(rev).complimentary()
        return rev_com
        
if __name__ == "__main__":
    seq = "ATCTCTGCACTAAT"
    a = test(seq)
    print(seq)
    print (a.reverse())
    print (a.complimentary())
    print (a.rev_comp())
    
