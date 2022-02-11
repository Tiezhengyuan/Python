#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:56:52 2020

@author: yuan
"""
a=np.arange(10);a
b=np.array([2]*10);b

#product and division
a*b#product
a/b#division
a//b#equal to np.floor(a/b)
a%b # equal to np.remainder(a,b)


#sum of np.array
np.add.reduce(a)#sum of a
sum(a) #sum of a
np.add.accumulate(a)#accumulative sum
a+b # add by another array

#product of np.array
a=np.arange(1,11);a
a.prod()# factorial of 10
np.arange(1,100).prod()#return zero when overflow
np.array([]).prod() #return 1 when it is empty array
a.cumprod() #cummulative factorial of value from 1-10

#minus
a
b
np.diff(a) #difference neighbouring elements
a-b# array is minus by another array

