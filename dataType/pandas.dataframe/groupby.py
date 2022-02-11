# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:09:27 2015

@author: yuan
"""


import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":
    #mid-term score
    df1=pd.DataFrame(np.random.randint(0,150, size=(15,5)), 
        columns=['english','math','science','social', 'physical'], 
        index=list("ABCDEFGHIJKLMNO"))
    df1['term']=['mid-term']*len(df1.index)
    df1['class']= list(pd.Series(['C1','C2','C3']).repeat(5))
    #final-term score
    df2=pd.DataFrame(np.random.randint(0,150, size=(16,5)), 
        columns=['english','math','science','social', 'physical'], 
        index=map(chr, range(65,81)))
    df2['term']=['final-term']*len(df2.index)
    df2['class']=list(df1['class'])+['C3']
    #combine data
    df=pd.concat([df1,df2])    
    df
        
    #group data by categorical data
    gr1=df.groupby('term')#group by term
    gr1.groups
    gr1.mean()#mean scores by term    
    df.groupby(df.index).sum()#sum of students of entire term
    df.groupby('class').agg(['mean', 'std'])
    df.groupby(['term','class']).agg(['mean','sum']).round()
        

    
    for row, row_index in gr1.groups.iteritems:
        print(row, list(df.iloc[row_index]))
    #print df_obj.size()
    #print df_obj.sum()
    #print df_obj.describe()
    #
    #print 'group by two factors:'
    df_obj=df.groupby(['A','B'])
    #print df_obj.groups
    
    #aggregation based groupby
    df_obj=df.groupby(['A','B'],as_index=False)
    #print df_obj.aggregate(np.sum)
    #print df_obj.aggregate([np.sum,np.mean])
    
    #agg based on groupby
    df_obj=df.groupby(['A','B'],as_index=False)
    #print df_obj.agg({'C':np.mean,'D':np.std})
    