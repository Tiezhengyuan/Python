#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:17:15 2020

@author: yuan
"""

#covariance matrix
x=np.array([1,2,3,4,5]);x #independent variable
y=np.array([0,4,4,7,10]);y #dependent variable
z=np.array([1,1,1,1,1]);y #uncorrelated variable
cov1=np.cov(x,y);cov1  #covariance matrix
cov1.trace()# sum of diagonal values
np.diagonal(cov1) #diagonal elements
cov1

#eigenvalues and eigenvectors
np.linalg.eig(cov1)[0] #eigenvalues
sum(np.linalg.eig(cov1)[0])
np.linalg.eig(cov1)[1] #eigenvectors

#uncorrelated x and y
cov2=np.cov(x,z);cov2  #covariance matrix
cov2.trace()# sum of diagonal values

#correlation coefficient matrix
x
y
np.corrcoef(x,y)
