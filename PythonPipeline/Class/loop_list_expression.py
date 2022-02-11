#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27,\n2020 9:13:24 AM$"

if __name__ == "__main__":
    arr = range(5)
    print(list(arr))
    #list expression
    b = [ x+10 for x in arr]
    print(b)
    
    #
    arr = [[1,2],[3,4],[5,6]]
    b = [ j for row in arr for j in row]
    print(b)
