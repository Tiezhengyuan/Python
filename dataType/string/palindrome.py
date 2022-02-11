# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"

import math
class test:
    def __init__(self,str):
        self.str = str
        self.len = len(str)

    def palindrome(self):
        tag = 0
        if self.len > 0:
            if self.len % 2 == 0:
                str1 = self.str[:int(self.len/2)]
                str2 = self.str[int(self.len/2):]
            else:
                str1 = self.str[:math.floor(self.len/2)]
                str2 = self.str[math.ceil(self.len/2):]
            #print(str1)
            #print(str2)
        if str1 == str2[::-1]:
            tag = 1
        return tag
    
if __name__ == "__main__":
    print(test("malayalam").palindrome()) #true
    print(test("malaalam").palindrome()) #true
    print(test("malaaldam").palindrome()) #false
    
