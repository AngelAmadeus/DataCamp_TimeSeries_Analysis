# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:39:07 2020

@author: User

Are Stock Prices a Random Walk?
Most stock prices follow a random walk (perhaps with a drift). You will look at 
a time series of Amazon stock prices, pre-loaded in the DataFrame AMZN, and run 
the 'Augmented Dickey-Fuller Test' from the statsmodels library to show that it 
does indeed follow a random walk.

With the ADF test, the "null hypothesis" (the hypothesis that we either reject 
or fail to reject) is that the series follows a random walk. Therefore, a low 
p-value (say less than 5%) means we can reject the null hypothesis that the 
series is a random walk.
"""

# Import the adfuller module from statsmodels
from statsmodels.tsa.stattools import adfuller
import pandas as pd

AMZN = pd.read_excel('AMZN.xlsx')
AMZN = pd.DataFrame(AMZN)

# Set date as index
AMZN = AMZN.set_index('Date')

# Run the ADF test on the price series and print out the results
results = adfuller(AMZN['Adj Close'])
print(results)

# Just print out the p-value
print('The p-value of the test on prices is: ' + str(results[1]))
