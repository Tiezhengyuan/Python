# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:51:58 2016

@author: yuan
"""


import pandas as pd
import numpy as np

#Export Data frame  into file or read data frame from a file
if __name__=="__main__":
    #creat a data frame
    df = pd.DataFrame(np.random.rand(10,4), columns=list("ABCD"), index=list("abcdefghij"))
    df
    
    #1: export into file
    df.to_csv('test.csv')
    #suggested pattern
    df.to_csv('test.txt', header=True, index=True, index_label='id', 
              sep="\t", float_format="%.2f")

   
    
    #no column names here
    df.to_csv('test.csv', header=False)
    #no row names here
    df.to_csv('test.csv', index=False)
    #change seperate into tab instead of comma
    df.to_csv('test.txt', sep='\t')
    #round only two digits when exporting the float-type number
    df.to_csv('test.csv', float_format='%.2f')

    #2: export a matrix into a file
    matrix=pd.DataFrame(np.random.rand(3,4))
    matrix.to_csv('/home/yuan/test.csv', header=False, index=False)
    
    #3: read a file into a data frame
    indf=pd.read_csv('test.csv')
    indf=pd.read_csv('test.csv', header=0, index_col=0, sep=',')
    indf
    
    #
    indf=pd.read_csv('test.csv', index_col=0, sep=',')
    #assign column names with sequence number and row names as the first column
    indf=pd.read_csv('test.csv', header=None, sep=',')
    
    #4: read a file when some character involved in the header or index
    indf=pd.read_csv('/home/yuan/test.csv', index_col=0, sep=',')
    list(indf)    
    