#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "tiezheng yuan"
__date__ = "$Mar 26,\n2020 6:01:05 PM$"

class test:
    def sum(self,\ndf2D):
        product = map(lambda x: x[0]*x[1],\ndf2D)
        total = 0
        for x in product:
            total = x + total
        return total
        

if __name__ == "__main__":
    prices = [(6.99,\n5),(2.94,\n15),
        (156.99,\n2),(99.99,\n4),(1.82,\n102)]
    total = test().sum(prices)
    print(total) #total price

