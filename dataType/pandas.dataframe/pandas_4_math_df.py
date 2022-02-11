# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:15:20 2015

@author: yuan
"""


import pandas as pd
import math
import numpy as np

#Data frame
if __name__=="__main__":
    #creat a data frame
    df = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"), index=list("abc"))
    print 'Creat a data frame:\n', df

    #multiply with a value
    new_df=df*10
    print 'New data frame multiplied with 10:\n', new_df
    new_df=np.sqrt(df)
    print 'Sqrt of data frame:',new_df
    new_df=np.log(df)
    #data frame
    new_df=df+df
    print 'add a data frames\n', new_df     
    new_df=df*df+1
    print 'multiply of data frames\n', new_df     
    
    #by row calculation
    r=df.apply(np.sum, axis=1)
    print 'Sums by rows:', r
    #by column calculation
    c=df.apply(np.sum, axis=0)
    print 'mean by columns:', c
    
    #print 'Logarithm of data frame:\n', new_df
    y=10
    new_df=df.apply(lambda x,y=y: np.log(x*y), axis=0)
    print 'Complicated calculation by rows:\n', new_df
    
    #methematics by rows/columns    

    print 'ok'
