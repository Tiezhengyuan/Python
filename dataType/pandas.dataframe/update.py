#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:49:12 2020

@author: yuan
"""


import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":
    
    #broadcasting features of df
    #firstly select and then revise
    
    #scores of mid-term exams
    df1 = pd.DataFrame(np.random.randint(20,150, 40).reshape(8,5), 
            columns=['english','math','science','social', 'physical'], 
            index=list("ABCDEFGH"))
    df1

    #update a row or column
    #the scores of student H are increased by 10%
    df1.loc[['H']] *= 1.1 
    #all enlighs scores are increased by 5
    df1.english += 5 
    
    #update some values using index/column
    #revise the math score of A to 60
    df1.loc['A','math'] = 60   
    #revise the science scores of C and D to 0
    df1.loc[['C','D']]['science'] = 0   

    #update some values using conditions
    #lift all scores <40 to 40
    df1.where(df1<40, 40)


