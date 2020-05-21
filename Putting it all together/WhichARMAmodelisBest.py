# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:26:20 2020

@author: User


Which ARMA Model is Best?

Recall from Chapter 3 that the Akaike Information Criterion (AIC) can be used 
to compare models with different numbers of parameters. It measures 
goodness-of-fit, but places a penalty on models with more parameters to 
discourage overfitting. Lower AIC scores are better.

Fit the temperature data to an AR(1), AR(2), and ARMA(1,1) and see which model 
is the best fit, using the AIC criterion. The AR(2) and ARMA(1,1) models have 
one more parameter than the AR(1) has.

The annual change in temperature is in a DataFrame chg_temp

"""

# Import the module for estimating an ARMA model
from statsmodels.tsa.arima_model import ARMA

import pandas as pd

chg_temp = pd.read_excel('chg_temp.xlsx')
chg_temp = chg_temp.set_index('DATE')


# Fit the data to an AR(1) model and print AIC:
mod_ar1 = ARMA(chg_temp, order=(1, 0))
res_ar1 = mod_ar1.fit()
print("The AIC for an AR(1) is: ", res_ar1.aic)

# Fit the data to an AR(2) model and print AIC:
mod_ar2 = ARMA(chg_temp, order=(2, 0))
res_ar2 = mod_ar2.fit()
print("The AIC for an AR(2) is: ", res_ar2.aic)

# Fit the data to an ARMA(1,1) model and print AIC:
mod_arma11 = ARMA(chg_temp, order = (1,1))
res_arma11 = mod_arma11.fit()
print("The AIC for an ARMA(1,1) is: ", res_arma11.aic)
