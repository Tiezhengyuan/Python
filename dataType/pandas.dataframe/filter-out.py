#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:41:33 2020

@author: yuan
"""


import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":
    #creat a data frame
    #scores of mid-term exams
    df = pd.DataFrame(np.random.randint(40,150, 75).reshape(15,5), 
            columns=['english','math','science','social', 'physical'], 
            index=list("ABCDEFGHIJKLMNO"))
    df
    
    #all failure students : any one of scores <60
    cond=df <= 60
    index=cond.any(axis=1)
    df[index]
    
    #qualified students: english and math scores >=60
    cond = df[['english','math']]>=60
    index = cond.any(axis=1)
    df[index]
    
    #all excellent student: mean>=90 and min>=60
    index=(df.mean(axis=1)>=90) & (df.min(axis=1)>=60)
    df[index]
    
    #select champions with highest scores on single course
    df.max(axis=0)
    index= df.idxmax(axis=0)
    df.loc[index]
    