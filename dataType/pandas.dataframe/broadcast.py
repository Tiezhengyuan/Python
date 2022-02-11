#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:16:33 2020

@author: yuan
"""

import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":
    #creat a data frame
    #scores of mid-term exams
    df1 = pd.DataFrame(np.random.randint(20,150, 40).reshape(8,5), 
            columns=['english','math','science','social', 'physical'], 
            index=list("ABCDEFGH"))
    df1
    #scores of final-term exams
    df2 = pd.DataFrame(np.random.randint(20,150, 45).reshape(9,5), 
            columns=['english','math','science','social', 'physical'], 
            index=list("ABCDEFGHI"))
    df2
    
    
    df1.shape
    df2.shape
    #the pattern would cause missing data
    df1+df2
    #handle missing data:
    df2.add(df1,fill_value=0)