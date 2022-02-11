# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"

import re
class test:
    def __init__(self,str):
        self.str = str
    
    def test(self):
        new = ''
        if (re.search('not(.*)poor', self.str)):
            new = re.sub('not(.*)poor', 'poor', self.str)
        elif ( 'good' in self.str):
            new = self.str.replace('good', 'poor')
        return new
        
        
if __name__ == "__main__":
    a= test("the lyrics is not that poor!").test()
    b = test("the lyrics is good!").test()
    print(a)
    print(b)
