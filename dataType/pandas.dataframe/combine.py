# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:43:14 2015

@author: yuan
"""

import pandas as pd

#pandas.merge()
#pandas.concat()
#pandas.append()
#pandas.combine_first()
#
if __name__=="__main__":
    #creat a data frame
    df1 = pd.DataFrame(np.random.randint(0,10, size=(3,4)), 
            columns=list("ABCD"), index=list("abc"))
    df2 = pd.DataFrame(np.random.randint(0,10, size=(4,3)), 
            columns=list("BaE"), index=list("adcf"))
    df3 = pd.DataFrame(np.random.randint(0,10, size=(3,4)), 
            columns=list("BADC"), index=list("cdb"))
    df4 = pd.DataFrame(np.random.randint(0,10, size=(3,4)), 
            columns=list("BADC"), index=list("cab"))    
    ###########1: concat()
    #concat() can be used for combining two or more data frames
    ##the parameter: axis, default axis=0
    ###columns or rows are matched to each other (different order doesn't matter )    
    pd.concat([df1,df1])
    pd.concat([df1,df3])
    pd.concat([df1,df3],axis=1)
    pd.concat([df1,df4],axis=1)
    #combine by column names, outer pattern
    pd.concat([df1,df2], axis=1)
    #combine by row names, outer pattern
    pd.concat([df1,df2], axis=0)
    #inner pattern
    pd.concat([df1,df2], axis=0, join='inner')
    pd.concat([df1,df2], axis=1, join='inner')

    
    ##########2: append()
    #append is a simple of concat() with only axis=0
    df1.append(df2)
    pd.concat([df1,df2])
    
    ##########3: the function merge()
    #default options
    df1.merge(df2)
    pd.merge(df1,df2)
    #
    pd.merge(df1,df2, left_index=True, right_index=True, how='left')
    #
    pd.merge(df1, df2, left_on='B', right_on='E', how='inner')
    #  
    pd.merge(df1,df2, on='B', how='outer')

    

    ###########4: the function join()
    #join() only used for combining two data frames without any sharing columns
    df1 = pd.DataFrame({'id':['a','a','b'], 'no':range(3)}, 
                        index=list('abc'))
    df2 = pd.DataFrame({'name':['a','b','c', 'd'], 'level':range(4)}, 
                        index=list('acbd'))
    df3 = df2.copy()
    df3.columns= ['name', 'level']
    #column names should be different or error aroused
    df1.join(df2)
    df2.join(df1)

    
    
    ####################################    
    #example 1 :just only combined two data frame even no row or column matched,
    df1 = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"), 
                       index=list('abc'))
    df2 = pd.DataFrame(np.random.rand(3,4), columns=list("BACD"))
    df3 = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"), 
                       index=list('abc'))

    #bind by column
    pd.concat([df1,df2])
    pd.concat([df1,df2], axis=1)
    #
    df1.reset_index(drop=True, inplace=True)
    df2.reset_index(drop=True, inplace=True)
    new_df=pd.concat([df1,df2], axis=1)