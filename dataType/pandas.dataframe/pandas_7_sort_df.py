# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:45:38 2016

@author: yuan
"""

import pandas as pd

if __name__ == "__main__":
    #create a data frame
    df = pd.DataFrame([{'c1':3,'c2':10}, {'c1':2, 'c2':30},
                            {'c1':1,'c2':20},{'c1':2,'c2':15},
                            {'c1':2,'c2':100}, {'c1':-2,'c2':10}])
    df.index=df['c1']
    print df
    
    ########sort rows
    #sort rows by columns
    sorted_df=df.sort(['c1','c2'], ascending=False)
    print sorted_df
    #
    sorted_df=df.sort(['c1','c2'], ascending=[False, True])
    print sorted_df
    
    #sort rows by row names
    sorted_df=df.sort_index(axis=0, ascending=True)
    print sorted_df

    #sort rows by row names
    #Note: row names should be unique with this method
    df.index=list('cdabfg')
    sorted_df=df.ix[sorted(df.index)]
    print sorted_df
    
    #sort rows by a given order
    sorted_df=df.ix[list('gxdacfa')]    
    print sorted_df
    
    ########sort columns
    #sort columns by column names
    sorted_df=df.sort_index(axis=1, ascending=False)
    print sorted_df
    
    #sort columns by column names
    sorted_df=df[sorted(df.columns, reverse=True)]
    print sorted_df
    
    
    #######other usages
    #in-place sorting using sort()
    df.sort(['c1','c2'], ascending=False, inplace=True)
    print df
    
    print 'ok\n'