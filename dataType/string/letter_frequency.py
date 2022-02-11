#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:38:46 AM$"

import re
class string:
    def __init__(self, str):
        self.str = str
    def freq(self):
        #keep letters only and combine upper/lower case
        letters = re.sub(r'\W+', '', self.str).upper()
        f = {} #store frequency into dictionary
        for i in letters:
            if i in f.keys():
                f[i] += 1
            else:
                f[i] = 1
        return f
        
        
if __name__ == "__main__":
    str = "Hello World. How are you today?"
    a = string(str).freq()
    print (a)
