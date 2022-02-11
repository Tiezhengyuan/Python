#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27, 2020 2:52:40 PM$"
#create array
import numpy as np

if __name__ == "__main__":
    #initiate a empty list by numpy
    np.array([])
    
    #np.arange()
    np.arange(10)# integer sequence from 0-9
    np.arange(5,10)#integer sequence from 5-9
    np.arange(1,20,3)#integer sequence from 1-20 increased by 3
    
    #np.zeros()
    np.zeros(10)
    np.zeros(5, dtype=int) # integer
    
    #np.ones()
    np.ones(10,dtype=float)# one sequence with float type    

    #arithmetics sequence
    np.linspace(1,100, num=5)

    #np.full()
    np.full( (3,6), 3.5, dtype=float)
    np.full(10, np.NaN)
    
    
    #initiate a zero matrix (3,6)
    np.zeros(shape=(3,6), dtype=np.int) #integer
    np.zeros((2,8), dtype=np.float64) # float


    #np.mat(): create a matrix
    np.mat('1 2 3; 4 5 6; 7 8 9')
    np.mat(np.arange(1,10).reshape(3,3))
    np.mat(np.zeros(9).reshape(3,3))
    
    #np.eye()
    np.eye(3, dtype=float)#create diagonal matrix
    

