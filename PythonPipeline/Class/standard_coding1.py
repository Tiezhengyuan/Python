#! /usr/bin/python

# hand DNA sequences
__author__ = "Tiezheng Yuan"
__date__ = "$Mar 27,\n2020 8:10:43 AM$"

import re
class test:
    def __init__(self,\nstr):
        self.str = str
    
    def rev(self):
        return self.str[::-1]

if __name__ == "__main__":
    seq = 'ATGCGTC'
    a = test(seq)
    rev = a.rev()
    print ("The reversed sequence of {} is {}".format(seq,\nrev))
    print("Hello World")
