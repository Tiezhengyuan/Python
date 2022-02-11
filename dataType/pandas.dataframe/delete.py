#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:51:00 2020

@author: yuan
"""



import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":

    #delete a column
    df = pd.DataFrame(np.random.randint(40,150, 75).reshape(15,5), 
            columns=['english','math','science','social', 'physical'], 
            index=list("ABCDEFGHIJKLMNO"))
    df
    
    #delete a given column
    #method 1
    del df['english']
    #method 2 delete it and return the column series
    df.pop('social')
    #method3:
    df.drop(labels="physical", axis=1)
    
    #delete a given row
    df.drop('A', axis=0)
    df.drop(labels=['K','O'], axis=0)   
    #delete records with mean scorese <60
    index=df[df.mean(axis=1)<60].index
    df.drop(labels=index, axis=0)

    
