#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:06:32 2020

@author: yuan
"""

import numpy as np

#4 rows and 8 columns
nd = np.round(np.random.rand(4,8)*100); nd

#index rows
nd[1,]#the 2nd row
nd[1:,] # the 2-4th rows
nd[2:]  #the 3-4th rows
nd[-1] # the last row

#index columns
nd[:,0]  # the 1st columns
nd[:,4:]  # the 5-8th columns
nd[:,-1]  # the last columns
nd[:,-2:]  # the last two columns

#part
nd1= nd[1:3,4:6];nd1 # part of ndarray
nd2= nd[1:3,4:6].copy();nd2 # deep copy
id(nd)
id(nd1)
id(nd2)

#slice
nd
nd[::-1]#reverse rows
nd[:,::-1]#reverse columns

nd[::2]# slice per 2 rows
nd[:,::2]# slice per 2 columns


