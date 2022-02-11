#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:04:43 2020

@author: yuan
"""
import pandas as pd
import numpy as np

#read data
infile = "/home/yuan/project/python_practise/data/allActionableVariants.txt"
df=pd.read_csv(infile, header=0, index_col=0, sep="\t")
df.iloc[:3,:]
df.iloc[:,9]
df.shape
list(df)

#
len(set(df['RefSeq'][~df['RefSeq'].isna()]))
#number of genes
cond1=~df['Entrez Gene ID'].isna()
len(set(df['Entrez Gene ID'][cond1]))

#
cond2=list(map(lambda x: 'Afatinib' in x, df['Drugs(s)']))
#df['Drugs(s)'][ cond1 & cond2]
#gene ids targetable by Afatinib
set(df['Entrez Gene ID'][ cond1 & cond2])

#cancer type: gene is BRAF, mutation at 600
cond3=df['Hugo Symbol']=='BRAF'
cond4=list(map(lambda x: '600' in x, df['Alteration']))
set(df['Cancer Type'][cond3&cond4])




