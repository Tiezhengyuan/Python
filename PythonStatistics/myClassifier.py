#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:49:45 2020

@author: yuan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, model_selection, neighbors
import scipy.stats as stats

import importlib
import myClassifier as mycl

#convert categorical data to numeric data
#return dictionary
def convert_categorical(x):
    #x =df['country']
    names=list(x.unique())
    #pairwise
    cat_dict=dict([ (name,index) for index, name in enumerate(names)])
    #
    cat_num=x.map(lambda x, y=cat_dict: y[x])
    return cat_num

#contigency table
def contigency_table(Y, Y_pred):
    a=Y+Y_pred
    tp=len(a[a==2])#true positive
    tn=len(a[a==0])#true negative
    b=Y-Y_pred
    fp=len(b[b==-1])#false positive
    fn=len(b[b==1])#false negative

    m = np.array([tp,fn, fp,tn]).reshape(2,2)
    md = pd.DataFrame(m,index=[['Predicton','Predicton'],['true', 'false']],
         columns=[['observation','observation'], ['true', 'false']]  )
    print(md)
    return m

#test best k of neighbors
def best_neighbors(X,Y, k_arr=np.arange(5,25,2)):
    #X=df_norm
    #k_arr=np.arange(5,50, 2)
    fisher=pd.DataFrame(np.zeros(shape=(len(k_arr),2)),
            index=k_arr, columns=['OR','pvalue'])
    #KNN
    for k in k_arr:
        knn = neighbors.KNeighborsClassifier(
                n_neighbors=k, weights='uniform')
        cls=knn.fit(X, Y)
        contigency=mycl.contigency_table(Y, cls.predict(X))
        fisher.loc[k]=stats.fisher_exact(contigency)
    #
    fisher['log10-pvalue'] = -np.log10(fisher['pvalue'])
    print(fisher)

    default_k= np.sqrt(X.shape[0])    
    #plot
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(15,5))
    #1
    fisher.plot(fisher.index, 'OR', ax=ax1)
    ax1.set_ylabel("odd ratio")
    ax1.axvline(default_k)
    #2
    fisher.plot(fisher.index, 'log10-pvalue', ax=ax2)
    ax2.axvline(default_k)
    ax2.set_ylabel("-log10 of p value")
    plt.suptitle('best k values')
    return fisher
    
