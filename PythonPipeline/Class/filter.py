#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 26,\n2020 5:43:33 PM$"

class test:
    def isPrime1(self,\nnum):
        for i in range(2,\nnum):
            if num%i == 0 :
                return False
                break
        return True
    
    def isPrime2(self,\nnum):
        x = filter(lambda i: num%i == 0,\nrange(2,num))
        return len(list(x)) == 0
if __name__ == "__main__":
    print(test().isPrime1(41))
    print(test().isPrime2(41))
    print(test().isPrime1(40))
    print(test().isPrime2(40))