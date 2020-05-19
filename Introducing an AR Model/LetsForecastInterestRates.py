# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:54:10 2020

@author: User


Let's Forecast Interest Rates

You will now use the forecasting techniques you learned in the last exercise 
and apply it to real data rather than simulated data. You will revisit a dataset 
from the first chapter: the annual data of 10-year interest rates going back 
56 years, which is in a Series called interest_rate_data. Being able to forecast 
interest rates is of enormous importance, not only for bond investors but also 
for individuals like new homeowners who must decide between fixed and floating 
rate mortgages.

You saw in the first chapter that there is some mean reversion in interest 
rates over long horizons. In other words, when interest rates are high, they 
tend to drop and when they are low, they tend to rise over time. Currently they 
are below long-term rates, so they are expected to rise, but an AR model attempts 
to quantify how much they are expected to rise.

"""

# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

interest_rate_data = pd.read_excel('interest_rate_data.xlsx')
interest_rate_data = pd.DataFrame(interest_rate_data)

# Set date as index
interest_rate_data = interest_rate_data.set_index('DATE')


# Forecast interest rates using an AR(1) model
mod = ARMA(interest_rate_data, order=(1,0))
res = mod.fit()

# Plot the original series and the forecasted series
res.plot_predict(start = 0, end = '2022')
plt.legend(fontsize=8)
plt.show()