# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:58:45 2016

@author: yuan
"""

# Load modules and data
import statsmodels.api as sm
data = sm.datasets.stackloss.load()
data.exog = sm.add_constant(data.exog)

# Fit model and print summary
rlm_model = sm.RLM(data.endog, data.exog[:,2], M=sm.robust.norms.HuberT())
rlm_results = rlm_model.fit()
rlm_results.params
rlm_results.summary()
rlm_results.rsquared()