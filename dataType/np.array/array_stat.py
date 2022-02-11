# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:50:56 2018

@author: yuan
"""

import numpy as np


a=np.random.rand(20);a
#attributes of an array
a.size#length of array
a.nbytes#bytes of array
a.ndim#number of dimesions

#statistics
np.mean(a) #mean value
np.var(a) #variance
np.median(a) #median
np.min(a) #minimum value
np.max(a) #maximum value
np.ptp(a) #range of array: maix-min

#Weighted average 
np.average([140,60,39], weights=[30,30,40])

