# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:08:56 2015

@author: yuan
"""


import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":
    #creat a data frame
    df = pd.DataFrame(np.random.rand(6,4), columns=list("ABCD"), index=list("abcdef"))
    print 'Creat a data frame:\n', df
    
    print '\nselect rows by columns using .loc:'
    new_df=df.loc[df['A']<.5,:]
    print new_df
    #multiple conditions
    new_df=df.loc[(df['A']<.5) & (df['B']<.5),:]
    print new_df
    new_df=df.loc[(df['A']<.5) & (df['A']<.5),:]
    print new_df
    
    
    print '\nselect columns by rows using .loc and .ix:'
    new_df=df.loc[:,df.ix['c']<.5]
    print new_df
    
    print '\nselect rows by columns using .ix:'
    new_df=df.ix[(df['A']<.3)]
    pirnt new_df
    
    #Function: where
    print '\nselect by using where():'
    new_df=df.where(df<0.5)
    print 'replace values with NaN meeting boolen:', new_df
