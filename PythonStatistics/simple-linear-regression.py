#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:31:21 2020

@author: yuan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing, model_selection

import importlib
import myLinearRegression as mylm

#1: get data
df = pd.read_csv('gapminder-FiveYearData.csv', header=0, index_col=False)
df.shape
df['log2-gdpPercap']= np.log2(df['gdpPercap'])
df['log2-pop']= np.log2(df['pop'])
#convert dummy variables
continents=list(pd.unique(df['continent']))
df=df.join(pd.get_dummies(df['continent']))
#
df.iloc[:3]


###################################################################
#observe: life expected
df.plot.scatter('log2-gdpPercap', 'lifeExp')
plt.hist(df['lifeExp'], 50)
plt.xlabel('expected life, year')
plt.ylabel('frequency')
#variable: gdpPercap
fig, (ax1,ax2)=plt.subplots(1,2)
ax1.hist(df['gdpPercap'], 50)
ax1.set_title('histograme of gdpPercap')
ax2.hist(np.log2(df['gdpPercap']),50)
ax2.set_title('log2 of gdpPercap')
#variable:
fig, (ax1,ax2)=plt.subplots(1,2)
ax1.hist(df['pop'], 50)
ax1.set_title('histograme of population')
ax2.hist(np.log2(df['pop']),50)
ax2.set_title('log2 of population')

#################################################################
#2: simple linear regression
X=df['log2-gdpPercap'].values.reshape(-1,1)
Y=df['lifeExp'].values.reshape(-1,1)
lm=linear_model.LinearRegression(fit_intercept=True)
#fit
reg=lm.fit(X, Y)
#
#predicted Y
predY=reg.predict(X)
predY.shape
#coefficients: slope
reg.coef_
reg.intercept_

importlib.reload(mylm)
coef_str=mylm.coef_str(reg)
#plot
df.plot.scatter('log2-gdpPercap', 'lifeExp', title="linear regression")
plt.plot(df['log2-gdpPercap'], reg.predict(X), color='black')
plt.text(8, 80, coef_str)


#residuals
res=Y-reg.predict(X)
#residual plot
importlib.reload(mylm)
mylm.residual_plot(Y, reg.predict(X))


##############################################################
#multiple linear regression
df.iloc[:3]
X1=df[['year','log2-pop', 'log2-gdpPercap']]
Y1=df['lifeExp'].values.reshape(-1,1)
lm=linear_model.LinearRegression(fit_intercept=True)
reg1=lm.fit(X1,Y1)
res1= Y1-reg1.predict(X1)
np.sum(res1**2)
reg1.coef_
reg1.intercept_

#residuals
res1=Y1-reg1.predict(X1)
#residual plot
importlib.reload(mylm)
mylm.residual_plot(Y1, reg1.predict(X1))

########################################3
#multiple linear regression+ categorical 
df.iloc[:3]
X2=df[['year','log2-pop', 'log2-gdpPercap']+continents]
Y=df['lifeExp'].values.reshape(-1,1)
lm=linear_model.LinearRegression(fit_intercept=True)
reg2=lm.fit(X2,Y)
res2= Y-reg2.predict(X2)
np.sum(res2**2) #RSS
reg2.coef_ #coefficient
reg2.intercept_

#residuals
res2=Y-reg2.predict(X2)
#residual plot
importlib.reload(mylm)
mylm.residual_plot(Y, reg2.predict(X2))

#cross validation
importlib.reload(mylm)
RSS_arr2, R2_arr2 = mylm.cross_validation(X2,Y, 50)

########################################3
#multiple linear regression+ categorical + polynomial regression
df.iloc[:3]
X3=df[['year']+continents]
Y=df['lifeExp'].values.reshape(-1,1)

poly= preprocessing.PolynomialFeatures(degree=2)
X3_poly=poly.fit_transform(df[['log2-pop', 'log2-gdpPercap']])
X3_poly=X3_poly[:,1:]
X3 = X3.join(pd.DataFrame(X3_poly, columns=[
        'log2-pop', 'log2-gdpPercap','pop*gdp','pop^2', 'gdp^2']))
X3.shape

lm=linear_model.LinearRegression(fit_intercept=True)
reg3=lm.fit(X3,Y)
reg3.coef_
reg3.intercept_

#residuals
res3=Y-reg3.predict(X3)
#residual plot
importlib.reload(mylm)
mylm.residual_plot(Y, reg3.predict(X3))

#cross validation
importlib.reload(mylm)
RSS_arr3, R2_arr3 = mylm.cross_validation(X3,Y, 50)

#cofidence interval
X=X3
RSS=np.sum(res3**2) #residual of sum of square
sample_size, coefs_num = X.shape
newX = pd.DataFrame({"Constant":np.ones(len(X))}).join(pd.DataFrame(X))
df=sample_size-coefs_num-1 #degree of freedom
MSE = RSS/df # mean of RSS

#predicted intervals using bootstrap 
importlib.reload(mylm)
coef=mylm.prediction_interval(X3,Y)
