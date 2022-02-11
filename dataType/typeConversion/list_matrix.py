# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:18:35 2015

@author: yuan
"""
import random 
import numpy as np

#list and 2D list
class mylist:
    
    def __init__(self):
        #generate random numbers
        self.arr=[]
        for i in range(50):
            value=random.randint(1, 10000)
            self.arr.append(value)
        print self.arr
    
    def To_2D(self, ncol=2):
        nrow=int(len(self.arr)/ncol)
        df=np.array(self.arr).reshape(nrow,ncol)
        print ('2D matrix:\n', df)
        return df
        
    def To_list(self, df):
        arr=np.array(df).ravel()
        print ('By rows:', arr)
        arr=np.array(df).ravel('F')
        print ('By columns:', arr)
        
#main program
cc=mylist()

#from list to matrix
df=cc.To_2D(ncol=5)

#fram matrix to list
cc.To_list(df)        
        
        
    