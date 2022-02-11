# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"
class test:
    def __init__(self,str):
        self.str = str
    
    def test(self):
        new = self.str
        if self.str[-3:] == 'ing':
            new = self.str + 'ly'
        else:
            new = self.str + 'ing'
        return new
        
        
if __name__ == "__main__":
    a = test("begin").test()
    b = test("string").test()
    print(a)
    print(b)
    
