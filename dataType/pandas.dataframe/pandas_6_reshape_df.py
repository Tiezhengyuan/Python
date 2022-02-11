# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:02:50 2015

@author: yuan
"""
import itertools
import numpy as np
import pandas as pd

if __name__=="__main__":
    
    #1: transpose a data frame: row to column and column to row
    #the function transpose()
    #df = pd.DataFrame(np.random.rand(5,4), columns=list("ABCD"), index=list("abcde"))
    #print 'Creat a data frame:\n', df
    #new_df=df.transpose()
    #print new_df
    
    #2: convert list and data frame
    #list to df: numpy.reshape()
    l=np.arange(12)
    df=pd.DataFrame(l.reshape(3,4))
    print 'list:',l
    print df
    #convert data frame to list
    #the order is row by row
    print df.values.tolist()
    print list(itertools.chain(*df.values.tolist()))
    
    #3: convert dictionary and data frame
    #dict to df
    # the length of nested list should be the same or error will be raised.
    d={'A':range(10), 'B': range(10)}
    print d
    df=pd.DataFrame(d)
    print df
    #df to dict
    print dict(df)

    #4:unpack variables: function of pandas.melt()
    df=pd.DataFrame({'age':[20,32,45],'name':['Hone','Jone','Joel'],'weight':[100,200,150]})
    print df
    print pd.melt(df, id_vars=['name'])
    
   
    print 'ok'