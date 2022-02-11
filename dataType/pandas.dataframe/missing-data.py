#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:49:42 2020

@author: yuan
"""

import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":
    #creat a data frame
    #scores of mid-term exams
    df = pd.DataFrame(np.random.randint(0,100, 75).reshape(15,5), 
            columns=['english','math','science','social', 'physical'], 
            index=list("ABCDEFGHIJKLMNO"))
    df['english']['K']=None
    df.loc['D','social']=None
    df
    
    #judge which cols don't contain nan
    df.notnull().all(axis=0)
    #judge which rows don't contain nan
    df.notnull().all(axis=1)
    #judge which columns invovle nan
    df.isnull().any(axis=0)
    #judge which rows invovle nan
    df.isnull().any(axis=1)
    
    #return rows containing nan
    df[df.isnull().any(axis=1)]
    #return columns containing nan
    df.loc[:,df.isnull().any(axis=0)]
    
    #discard rows containing nan
    df[df.notnull().all(axis=1)]
    #discard cols containing nan
    df.loc[:,df.notnull().all(axis=0)]
    
    #fill nan with zero
    df.fillna(value=0)
    #fill nan with median value along column
    df.fillna(value=df.median(axis=0))
    #fill nan with before value along column
    df.fillna(method='bfill')
    

    