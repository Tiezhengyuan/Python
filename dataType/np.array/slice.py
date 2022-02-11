#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:17:28 2020

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
    
    df1
    #only slice rows rahter than columns
    #slice per 2 rows and return the first row
    df1[::2]
    #reverse the order of rows
    df1[::-1]
    #reverse the order of rows, slice per 3 rows and return the first row
    df1[::-3]
    
    
    