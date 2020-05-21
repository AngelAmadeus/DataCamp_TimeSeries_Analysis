# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:39:46 2020

@author: User


Don't Throw Out That Winter Coat Yet

Finally, you will forecast the temperature over the next 30 years using an 
ARMA(1,1) model, including confidence bands around that estimate. Keep in mind 
that the estimate of the drift will have a much bigger impact on long range 
forecasts than the ARMA parameters.

Earlier, you determined that the temperature data follows a random walk and you 
looked at first differencing the data. In this exercise, you will use the ARIMA 
module on the temperature data (before differencing), which is identical to 
using the ARMA module on changes in temperature, followed by taking cumulative 
sums of these changes to get the temperature forecast.

The data is preloaded in a DataFrame called temp_NY.
"""

# Import the ARIMA module from statsmodels
from statsmodels.tsa.arima_model import ARIMA

import matplotlib.pyplot as plt
import pandas as pd

temp_NY = pd.read_excel('temp_NY.xlsx')
temp_NY = temp_NY.set_index('DATE')

# Forecast temperatures using an ARIMA(1,1,1) model
mod = ARIMA(temp_NY, order=(1,1,1))
res = mod.fit()

# Plot the original series and the forecasted series
res.plot_predict(start='1872', end='2046')
plt.show()
