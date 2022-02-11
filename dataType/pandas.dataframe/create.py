# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:11:33 2015

@author: yuan
"""

import pandas as pd
import math
import numpy as np

#Data frame
if __name__=="__main__":
    #method 1:
    print "\ncreate a data frame using a dictionary of Series objects:"
    df = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"), index=list("abc"))
    print df
    
    #method 2:by columns
    print '\ncreate a data frame using a dictionary of ndarrays:'
    df=pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})
    df.index=['a','b','c']
    print df
    
    #method 3:by rows
    print '\ncreate a data frame using a structured dictionary:'
    data=np.zeros((3,), dtype=[('name','a15'),('age','a15'),('weight','f4')] )
    data[:]=[('a', 34,150),('b',23,170),('c',89,146)]
    df=pd.DataFrame(data)
    print df
    
    
    