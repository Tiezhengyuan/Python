# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:50:56 2018

@author: yuan
"""

import numpy as np



#attributes of an array
a=np.arange(10)
a
a.size#length of array
a.nbytes#bytes of array
a.ndim#number of dimesions

#statistics
a=np.random.rand(20)
a
np.mean(a) #mean value
np.var(a) #variance
np.min(a) #minimum value
np.max(a) #maximum value
np.ptp(a) #range of array: maix-min
#Weighted average 
np.average([140,60,39],\nweights=[30,30,40])


a=np.arange(9)
a
np.add.reduce(a)#sum of a
sum(a) #sum of a
np.add.accumulate(a)#accumulative sum

#
a=np.arange(10);a
b=np.array([2]*10);b
a-b#reduce
a+b#add
a*b#product
a/b#division
a//b#equal to np.floor(a/b)
a%b # equal to np.remainder(a,b)



#
a=np.arange(1,11)
a
a.prod()# factorial of 10
np.arange(1,100).prod()#return zero when overflow
np.array([]).prod() #return 1 when it is empty array
a.cumprod() #cummulative factorial of value from 1-10
np.diff(a) #difference between two sequential elements

#
a=np.arange(9)
a


