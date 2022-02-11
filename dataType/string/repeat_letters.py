# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"
class test:
    def __init__(self,str):
        self.str = str
    
    def test(self, length, times):
        last_str = self.str[-length:]
        return last_str * times
        
        
if __name__ == "__main__":
    a = test("Hello").test(3,4)
    print (a)
    
