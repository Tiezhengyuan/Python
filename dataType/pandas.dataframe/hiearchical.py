#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:00:13 2020

@author: yuan
"""

import numpy as np
import pandas as pd

#mid-term score
df1=pd.DataFrame(np.random.randint(0,150, size=(15,5)), 
 columns=['english','math','science','social', 'physical'], 
 index=list("ABCDEFGHIJKLMNO"))

#final-term score
df2=pd.DataFrame(np.random.randint(0,150, size=(15,5)), 
 columns=['english','math','science','social', 'physical'], 
 index=map(chr, range(65,80)))

#create hierachical df
df=pd.DataFrame(np.random.randint(0,150, size=(30,5)), 
 columns=['english','math','science','social', 'physical'], 
 index=pd.MultiIndex.from_product(
         [list("ABCDEFGHIJKLMNO"), ['mid-term','final-term']]
         ))

#
list(df)#col names
list(df.index)
list(pd.MultiIndex.from_tuples(df.index).levels[0])
list(pd.MultiIndex.from_tuples(df.index).levels[1])

#index
df['math']
df['math']['O', 'mid-term']
df.loc['O', 'mid-term']['math']

#sclice
df.loc[::2,::1] #only mid-term scores
df.loc[::-2,::1] #only final-term scores

#reshape: row<->columns
df.stack(level=0)#col->row
df.unstack(level=1)#row->col

#statistics
df.mean(axis=0, level=0) #mean of student scores of two terms
df.mean(axis=0, level=1) #mean of mid-/final-term scores
df.sum(axis=1).mean(level=0)# mean of total scores of each student


