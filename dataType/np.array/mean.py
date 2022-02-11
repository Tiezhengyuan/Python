#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:24:10 2020

@author: yuan
"""

#
a=np.arange(12).reshape(3,4);a

#mean of entire data
np.mean(a)
a.mean()

#mean is calculated along the same columns
np.mean(a, axis=0)
#mean is calculated along the same rows
np.mean(a, axis=1)
#nan
a=[1,23, 4, np.nan]
np.mean(a)
np.nanmean(a)

#Inf:  # treate data in advance
a = np.arange(12).reshape(3,4);a
#method1
b = a.copy()
b[b==0]=1
b = np.log(b)
np.mean(b, axis=0)

#method2
b = np.log(a);b
b[np.isinf(b)]=0;b
np.mean(b, axis=0)

