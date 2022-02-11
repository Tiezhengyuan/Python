#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:50:43 2020

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
    
    
    #score means per course in mid-term
    df1.mean(axis=0)
    #score means of students in mid-term
    df1['mean']=df1.mean(axis=1)
    df1['total']=df1.sum(axis=1)
    df1['min']=df1.min(axis=1)
    df1['max']=df1.max(axis=1)
    df1