# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"
class test:
    def __init__(self,str):
        self.str = str
    
    def test(self):
        pass
        
        
if __name__ == "__main__":
    str = "Hello world!"
    print ("the first 2 letters: ", str[:2])
    print ("remove the last 2 letters: ", str[:-2])
    print ("the last 1 letter: ", str[-1:])
    print ("the 3-7 letters: ", str[2:7])
    print ("the 4-end letters: ", str[3:])
    print ("the 1-7 letters: ", str[:7])
    print ("remove the first 2 and last 2 letters: ", str[2:-2])
    
    
