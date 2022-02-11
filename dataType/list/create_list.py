# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:17:40 2016

@author: yuan
"""
#variable type in python
#numbers, string, list, dictionary, data frame

#initiate a empty list
l=[];print(l)
l= ['a', 'b','3'];print(l)
#initiate a list as a sequence with 2 step
l=list(range(10,100,2));print(l)
#initiate a list with 20 elements and all elements are set as 4
l=[4 for x in range(20)];print(l)
l=[4]*10;print(l)
#initiate a list with 10 elements and all elements are set as 'no'
l=['no' for x in range(10)];print(l)
l=['yes']*10;print(l)
