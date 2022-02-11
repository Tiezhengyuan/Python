# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Feb 7,\n2020 6:56:46 PM$"

import time


def test(x):
    return float(x)*3.5

if __name__ == "__main__":
    arr=range(1,1000000)
    arr2=[]
    
    #method1: for loop
    start1=time.time()
    for x in arr:
        arr2.append(test(x))
    print(time.time()-start1)
    
    #method2: map
    start2=time.time()
    arr2=list(map(test,\narr) )
    print(time.time()-start2)
    
