# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:43:14 2015

@author: yuan
"""

import pandas as pd

#pandas.merge()
#pandas.concat()
#pandas.combine_first()

if __name__=="__main__":
    #creat a data frame
    df1 = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"), index=list("abc"))
    df2 = pd.DataFrame(np.random.rand(3,4), columns=list("BACD"), index=list("cba"))
    print df1
    print df2
    
    ###columns or rows are matched to each other (different order doesn't matter )    
    #combine by columns
    new_df=pd.concat([df1,df[2], axis=1)
    print 'Combined data frame by columns:\n', new_df
    #combine by rows
    new_df=pd.concat([df1,df2], axis=0)
    print 'Combined data frame by rows:\n', new_df
    
    
    #### columns or rows might be different
    #combine data frames, and get combine columns
    #match between row names, and get unique row names
    new_df=pd.concat([df1,df2], axis=1)
    print 'Combined data frame by columns:\n', new_df
    
    #combine data frames, and get combine rows
    #match between column names, and get unique column names
    df2 = pd.DataFrame(np.random.rand(3,4), columns=list("ABEF"), index=list("cbd"))    
    print df1, df2    
    new_df=pd.concat([df1,df2], axis=0)
    print 'Combined data frame by rows:\n', new_df

    #creat a data frame
    df1 = pd.DataFrame({'id':['a','a','b','b','c','c'], 'no':range(6)})
    df2 = pd.DataFrame({'id':['a','b','c'], 'level':range(3)})
    #merge data frame by intersections
    new_df=pd.merge(df1,df2, on='id')
    print df1,df2, new_df
    
    #merge data frame if index is overally matched. rownames would be intersections between them
    df1 = pd.DataFrame({'id':['a','a','b','b','c','c'], 'no':range(6)})
    df2 = pd.DataFrame({'id':['a','b','d'], 'level':range(3)})
    new_df=pd.merge(df1,df2, on='id')
    print df1, df2, new_df
   
    #if you want all include, add another swich
    new_df=pd.merge(df1,df2, on='id', how='outer')
    print df1, df2, new_df   
    
    #if the colnames are not the same using the switches of 'left_on' and 'right_on'
    df1 = pd.DataFrame({'id1':['a','a','b','b','c','c'], 'no':range(6)})
    df2 = pd.DataFrame({'id2':['a','b','c'], 'level':range(3)})
    new_df=pd.merge(df1,df2, left_on='id1', right_on='id2')
    print new_df    
    
    #if two factors used for merging
    df1 = pd.DataFrame({'id1':['a','a','b','b','c','c'], 'id2':['E','E','F','F','G','G'], 'no':range(6)})
    df2 = pd.DataFrame({'id1':['a','b','c'], 'id2':['E','F','G'], 'level':range(3)})
    new_df=pd.merge(df1,df2, on=['id1','id2'])
    print new_df     
    
    #merge data frame by one column of a data frame and row names of another data frame
    df1 = pd.DataFrame({'id1':['a','a','b','b','c','c'], 'id2':['E','E','F','F','G','G'], 'no':range(6)})
    df2 = pd.DataFrame(['E','F','G'],columns=['id2'],index=['a','b','c'])
    new_df=pd.merge(df1,df2, left_on='id1', right_index=True)
    print new_df