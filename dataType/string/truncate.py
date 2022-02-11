# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"
class test:
    def __init__(self, str):
        self.str = str
    
    def test(self, n):
        #the first n letters, and last n leters
        s = ''
        if (len(self.str) > 2):
            s = self.str[:n] + self.str[-n:]
        return s
        
        
if __name__ == "__main__":
    str = "Hello World"
    s = test(str).test(2)
    print(s)
    
