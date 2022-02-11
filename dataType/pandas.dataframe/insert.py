#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:25:16 2020

@author: yuan
"""




import pandas as pd
import numpy as np

#Data frame
if __name__=="__main__":

    #delete a column
    df = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"), index=list("abc"))
    df
    
    #insert a column
    df = pd.DataFrame(np.random.rand(3,4), columns=list("ABCD"), index=list("abc"))
    df.insert(1, 'E', [245,7,2])
    print 'insert a column using insert():', df