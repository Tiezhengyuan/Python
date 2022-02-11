# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:50:00 2018

@author: yuan
"""

import numpy as np



#arithmatics
a=np.mat(np.arange(1,10).reshape(3,3));a
b=np.mat(np.ones(9).reshape(3,3));b
a+b#add of matrix
a-b#reduce
a*b#product

#invert matrix
a=np.mat('0 1 2; 1 0 3; 4 -3 8');a
a_invert=np.linalg.inv(a);a_invert
a*a_invert


#eigenvalues
a=np.mat('3 -2;1 0');a
np.linalg.eigvals(a)#eigenvalues
np.linalg.eig(a)[1] #eigenvectors
#SVD
a=np.mat('4 11 14; 8 7 -2');a
U,sigma,V=np.linalg.svd(a)
U
sigma
V





