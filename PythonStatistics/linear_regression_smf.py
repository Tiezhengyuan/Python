# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:02:11 2017

@author: yuan
"""
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

if __name__=='__main__':
    #read data frmae
    infile='/home/yuan/results_phip/phipseq6_human/statistics/lowRC_pep_scalingRC.txt'
    indf=pd.read_csv(infile,sep='\t', index_col=0)
    indf.shape
    
    #observe the data
    NC_median=indf.ix[:,0:8].apply(np.median, axis=1)
    NC_std=indf.ix[:,0:8].apply(np.std, axis=1)
    NC=pd.DataFrame({'median':NC_median,'std':NC_std})
    
    #
    formula='std~median'
    model=smf.ols(formula, data=NC)
    results=model.fit()
    print(results.summary())
    #predict values of dependentable variables based on the fitted model
    NC['pred_std']=results.predict()
    #or: NC['pred_std']=model.predict(results.params)
    #or model.predict(results.params, sm.add_constant(range(100)))
    
    #get parameters
    print('Intercept=', results.params['Intercept'])
    print('Slope=', results.params['median'])
    print('R2=', results.rsquared)
    residuals=NC['std']-NC['pred_std']
    std_res=np.std(residuals)
    print("STD of residuals=", std_res)
    
    params='Intercept={}\nSlope={}\nR2={}'.format(results.params['Intercept'], \
                      results.params['median'], results.rsquared)
    
    #present the fitting model
    plt.clf()
    plt.ylim(-5,10)
    plt.plot(NC['median'], NC['std'], 'p')#observed
    plt.plot(NC['median'], NC['pred_std'], 'r-')#regressed
    plt.text(40,40,  params)
    plt.xlabel('Median')
    plt.ylabel('Standard deviation')
    plt.title('Linear regression')
    plt.show()
    
    
    #default fitting include intercept and slope
    #force intercept is zero
    formula='std~median-1'
    model=smf.ols(formula, data=NC)
    results=model.fit()
    print(results.summary())
    print(results.params)
    
    #
    formula='np.log(std)~np.log(median)'
    model=smf.ols(formula, data=NC)
    results=model.fit()
    print(results.summary())
    print(results.params)

    print 'ok'