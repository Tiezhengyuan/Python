# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:48:48 2015

@author: yuan
"""

import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":
    #creat a data frame
    df = pd.DataFrame(np.random.rand(5,4), columns=list("ABCD"), index=list("abcde"))
    df['E']=[np.nan]*5
    print 'Creat a data frame:\n', df
    """
    #1 replace condition: values below .5 replaced with 10
    #replace all values of the whole df
    df[df<=.5]=100

    #replace column 'C' only if column 'A' meet the condition
    df['C'][df['A']<=.5]=100
    
    #replace whole df only if column 'A meets the condition
    df[df['A']<=.5]=100
    
    #replace 'C' and 'D' only if 'A'<=.5 and 'B'<=.5
    #set values with slices of a data frame
    df.loc[(df['A']<=.5)&(df['B']<=.5), ['C','D']]=100
    
    #drop na with 0
    df=df.fillna(0)
    
    #drop inf with 0
    df=df/0 # divided by 0
    print df
    #replace all inf with 10
    df=df.replace([np.inf,-np.inf],10)
    
    """"
    #
    print df    
    print 'ok'
