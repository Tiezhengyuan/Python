# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"

import re
class test:
    def __init__(self,str1, str2):
        self.str1 = str1
        self.str2 = str2
    
    def method1(self):
        a = list(self.str1)
        a.sort()
        a_str = "".join(a)
        b = list(self.str2)
        b.sort()
        b_str = "".join(b)
        return a_str == b_str
    
    def method2(self):
        tag = 1
        while len(self.str1)>0 and len(self.str2)>0:
            letter = self.str1[0]
            self.str1=self.str1.replace(letter, "")
            self.str2=self.str2.replace(letter, "")
            if len(self.str1) != len(self.str2):
                tag = 0
                break
        return tag
        
if __name__ == "__main__":
    print(test("cinema","iceman").method1())
    print(test("cinema","iceman").method2())
    print(test("cinema","icemacn").method2())
    print(test("cinema","icemac").method2())
    print(test("cinedma","iceman").method2())
    
