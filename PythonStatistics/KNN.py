#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:48:52 2020

@author: yuan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, model_selection, neighbors
import scipy.stats as stats

import importlib
import myClassifier as mycl

#1: get data
df = pd.read_csv('gapminder-FiveYearData.csv', header=0, index_col=False)
df.shape

#convert categorial data to numeric data
importlib.reload(mycl)
df['country_num']=mycl.convert_categorical(df['country'])
df['continent_num']=mycl.convert_categorical(df['continent'])
df.iloc[:3]

#normalization using z-score
df_num=df[df.columns.difference(['country','continent', 'lifeExp'])]
df_norm=preprocessing.StandardScaler().fit_transform(df_num)
df_norm=pd.DataFrame(df_norm, columns=df_num.columns)
df_norm.iloc[:3]

#K-nearest neghbors classification
knn = neighbors.KNeighborsClassifier(n_neighbors=5, weights='uniform')
Y=df['lifeExp'].map(lambda x: 0 if x>=70 else 1)
X_train,X_test,Y_train,Y_test=model_selection.train_test_split(df_norm, Y, test_size=.1)
cls=knn.fit(X_train, Y_train)
Y_pred=cls.predict(X_test)

#contigency table
importlib.reload(mycl)
m=mycl.contigency_table(Y_test, cls.predict(X_test) )
#fisher exact test
OR, pvalue=stats.fisher_exact(m)

#test the best k value
importlib.reload(mycl)
OR_k=mycl.best_neighbors(X,Y, np.arange(5,50, 2))



