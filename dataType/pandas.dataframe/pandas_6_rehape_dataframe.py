# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:02:50 2015

@author: yuan
"""
import numpy as np
import pandas as pd

if __name__=="__main__":
    
    #list to data frame
    l=np.arange(12)
    df=pd.DataFrame(l.reshape(3,4))
    print 'list:',l
    print df
    
    #transpose a data frame
    new_df=df.transpose()
    print new_df