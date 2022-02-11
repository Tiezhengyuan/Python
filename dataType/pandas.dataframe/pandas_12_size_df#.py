# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:40:35 2016

@author: yuan
"""

import numpy as np
import pandas as pd
import sys
import random
import scipy as sp
import scipy.sparse as sps

#memory usage of data frame
#how to store huge data frame or matrix

def create_dataframe(d=100):
    dimension=(d,d)
    #create zeros dataframe using numpy
    if (d<1e6):
        matrix=np.zeros(dimension, dtype=np.int8)
        #print matrix
    else:#create data frame using sci if huge matrix
        #return a dense matrix
        matrix=sps.csr_matrix(dimension, dtype=np.int8).todense() 
    #convert to pandas data frame
    df=pd.DataFrame(matrix)
    #print df
    #
    return df
    


#main program
#empty data frame with zeros
df1=create_dataframe(1e5)
size=int(sys.getsizeof(df1))
print "Size of zeros data frame is %d byte" % size

df2=create_dataframe(1e5)
size=int(sys.getsizeof(df2))
print "Size of zeros data frame is %d byte" % size

print 'ok'