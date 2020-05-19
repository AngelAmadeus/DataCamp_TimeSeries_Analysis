# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:05:41 2020

@author: User

How About Stock Returns?
In the last exercise, you showed that Amazon stock prices, contained in the 
DataFrame AMZN follow a random walk. In this exercise. you will do the same 
thing for Amazon returns (percent change in prices) and show that the returns 
do not follow a random walk.

"""
# Import the adfuller module from statsmodels
from statsmodels.tsa.stattools import adfuller
import pandas as pd

AMZN = pd.read_excel('AMZN.xlsx')
AMZN = pd.DataFrame(AMZN)

# Set date as index
AMZN = AMZN.set_index('Date')

# Create a DataFrame of AMZN returns
AMZN_ret = AMZN.pct_change()

# Eliminate the NaN in the first row of returns
AMZN_ret = AMZN_ret.dropna()

# Run the ADF test on the return series and print out the p-value
results = adfuller(AMZN_ret['Adj Close'])
print('The p-value of the test on returns is: ' + str(results[1]))



