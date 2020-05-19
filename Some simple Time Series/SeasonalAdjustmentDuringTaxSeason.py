# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:31:12 2020

@author: User

Seasonal Adjustment During Tax Season
Many time series exhibit strong seasonal behavior. The procedure for removing 
the seasonal component of a time series is called seasonal adjustment. For 
example, most economic data published by the government is seasonally adjusted.

You saw earlier that by taking first differences of a random walk, you get a 
stationary white noise process. For seasonal adjustments, instead of taking 
first differences, you will take differences with a lag corresponding to the 
periodicity.

Look again at the ACF of H&R Block's quarterly earnings, pre-loaded in the 
DataFrame HRB, and there is a clear seasonal component. The autocorrelation is 
high for lags 4,8,12,16,... because of the spike in earnings every four quarters 
during tax season. Apply a seasonal adjustment by taking the fourth difference 
(four represents the periodicity of the series). Then compute the autocorrelation 
of the transformed series.

"""
# Import the adfuller module from statsmodels
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

HRB = pd.read_excel('HRB.xlsx')
HRB = pd.DataFrame(HRB)

# Set date as index
HRB = HRB.set_index('Quarter')

# Seasonally adjust quarterly earnings
HRBsa = HRB.diff(4)

# Print the first 10 rows of the seasonally adjusted series
print(HRBsa.head(10))

# Drop the NaN data in the first four rows
HRBsa = HRBsa.dropna()

# Plot the autocorrelation function of the seasonally adjusted series
plot_acf(HRBsa)
plt.show()
