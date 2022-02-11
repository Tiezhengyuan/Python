#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Apr 14, 2020 2:08:51 PM$"

if __name__ == "__main__":
    
    #random numbers
    # N dimensional matrix
    
    #random numbers with uniform distribution
    np.random.rand(10,1)#1D, 10 rows, 1 columns
    np.random.rand(3,5)#2D, 3 rows, 5 columns
    np.random.rand(3, 2, 5)#3D
    
        
    # random number with normal distribution (u=0, var=1)
    np.random.randn(10,1)#1D, 10 rows, 1 columns
    np.random.randn(3,5)#2D, 3 rows, 5 columns
    np.random.randn(3, 2, 5)#3D
        
    #1D array 
    #0-1 random float numbers with uniform distributed
    np.random.random(size=10)
    #given ranged integer numbers with uniform distributed
    np.random.randint(1,5,8)
    #standard normal distribution with mean=0 and var=1
    np.random.normal(0, 1, size=10)