# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:09:27 2015

@author: yuan
"""


import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":
    #create a data frame
    df = pd.DataFrame({
        'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo','foo'],
        'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'two', 'one','three'],
        'C' : np.random.randn(10), 'D' : np.random.randn(10)*10})
    df.index=range(10,18)
    print df.shape
    print df
    
    #########1: the function groupby()
    print '\ngroup data frame into dictionary using groupby():'
    #group by the column known as 'A'
    df_obj=df.groupby('A')
    print df_obj.groups
    for row, row_index in df_obj.groups.iteritems():
        #print row, list(df.ix[row_index,'C'])
        print row, df.ix[row_index,]
    print df_obj.describe()
    print df_obj.size()
    print df_obj.count()
    print df_obj.sum()
    print df_obj.mean()
    print df_obj.max()
    print df_obj.median()

    #'group by two factors:'
    df_obj=df.groupby(['A','B'])
    print df_obj.groups
    
    ########2: the functions aggregate() and groupby() combined
    df_obj=df.groupby(['A','B'],as_index=False)
    print df_obj.sum()
    print df_obj.aggregate(np.sum)
    print df_obj.aggregate([np.sum,np.mean,np.median,np.max])
    
    #collpase df by rows on different patterns
    df_obj=df.groupby(['A','B'],as_index=False)
    print df_obj.aggregate({'C':np.mean,'D':np.std})
    
    
    ########Example 1: collapse a data frame
    df = pd.DataFrame(np.random.rand(10,4), columns=list("ABCD"), index=list("abcdefghij"))
    df.insert(0, 'group', list('ooonnnnaaa') ) # insert a column
    print df
    #group by
    df_obj=df.groupby(['group'], as_index=False)
    #calculate pattern
    cvdf=df_obj.aggregate(lambda x: np.std(x)/np.mean(x))  # caclculate CV  
    #set index
    cvdf=cvdf.set_index('group') #rename row names
    print cvdf

    