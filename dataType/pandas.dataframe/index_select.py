# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:48:48 2015

@author: yuan
"""

import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":
    #creat a data frame
    #scores of mid-term exams
    df1 = pd.DataFrame(np.random.randint(20,150, 40).reshape(8,5), 
            columns=['english','math','science','social', 'physical'], 
            index=list("ABCDEFGH"))
    df1
    #scores of final-term exams
    df2 = pd.DataFrame(np.random.randint(20,150, 45).reshape(9,5), 
            columns=['english','math','science','social', 'physical'], 
            index=list("ABCDEFGHI"))
    df2

    
   
    #index by columns using different methods
    #Note: return is Series structure
    #column is attribute of data frame
    df1.math #scores of math
    df1['math'] #math column
    df1[['physical','social']] # scores of physical and social
    df1.iloc[:,1] #math column
    df1.iloc[:,-1] # the last column
    
    #row: index
    df1.loc['A'] # the row with index A
    df1.loc[['A', 'B']] # the rows of A and B
    df1.iloc[2] # the row of C
    df1.iloc[[2,6]] # the rows of C and G
    df1.iloc[3:5] # the 4-5th rows
    df1.iloc[-1]  # the last row
    
    #index row and col combined
    df1['math']['C']#scores of english of C
    df1.loc['C']['math']#scores of english of C
    df1.loc['C','math']#scores of english of C
    
