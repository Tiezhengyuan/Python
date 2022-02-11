#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27,\n2020 2:52:40 PM$"
#create array
import numpy as np

if __name__ == "__main__":
    #initiate a empty list by numpy
    l=np.array([])
    np.arange(10)# integer sequence from 0-9
    np.arange(5,10)#integer sequence from 5-9
    np.arange(1,20,3)#integer sequence from 1-20 increased by 3
    np.zeros(10)# zero sequence
    np.ones(10,dtype=float)# one sequence with float type
    #initiate a zero list with 5 elements
    l=np.zeros(5,\ndtype=int8)
    np.random.rand(10,1)#random sequence within 0-1
    np.random.normal(0,\n1,\n10)#standard normal distribution with mean=0 and var=1
