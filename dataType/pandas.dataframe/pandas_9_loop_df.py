# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:55:33 2016

@author: yuan
"""
import numpy as np
import pandas as pd

if __name__ == "__main__":
    #create a data frame
    df = pd.DataFrame([{'c1':3,'c2':10}, {'c1':2, 'c2':30},
                            {'c1':1,'c2':20},{'c1':2,'c2':15},
                            {'c1':2,'c2':100}, {'c1':-2,'c2':10}])
    df.index=range(10,16)
    print df
    
	###### 1: for loop
    #loop by rows
    for row_name, row in df.iterrows():
        #print list(df.ix[row_name])
        #print row_name
        print '_'.join(str(x) for x in row)


    #loop by columns
    for col_name, col in df.iteritems():
        print col
        s=pd.Series(list(df[col_name]))
        s.index=range(10,16)
        #print s

        
    ########2: the function: apply
    #loop by rows and counts the number of values beyond threshold
    counts=df.apply(lambda x, y=2: len(x[x>=y]), axis=0)
    counts
    #another patterns
    counts=df.apply(lambda x, y: len(x[x>=y]), args=(2,), axis=0)
    counts
    
    print "ok"
