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
    
    #delete a column
    df = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"), index=list("abc"))
    print df
    del df['A']
    print 'delete a column using del:', df
    df.pop('C')
    print 'delete a column using pop():', df
    df=df.ix[:,1:]
    print 'delete the first column using index:', df
    
    #delete a row
    print df
    df.drop('a')    
    print 'delete a row using drop():', df
    df=df[1:]
    print 'delete the first row:', df
    
    #insert a column
    df = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"), index=list("abc"))
    df.insert(1, 'E', [245,7,2])
    print 'insert a column using insert():', df
    
    print 'ok'
    
    