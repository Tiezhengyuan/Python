#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:28:00 2020

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

       
    #Name of columns and rows
    list(df1.index) #row names
    df1.index=list('abcdedgh')#change row names
    
    list(df1)#show column names
    df1.columns=list('EMSSP')#change column names

    #change a specific column or row name 
    df1=df1.rename(columns={'S':'SS'})
    df1=df1.rename(index={'b':'c'})
    df1
    