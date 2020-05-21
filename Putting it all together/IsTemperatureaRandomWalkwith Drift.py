# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:41:02 2020

@author: User



Is Temperature a Random Walk (with Drift)?

An ARMA model is a simplistic approach to forecasting climate changes, but it 
illustrates many of the topics covered in this class.

The DataFrame temp_NY contains the average annual temperature in Central Park, 
NY from 1870-2016 (the data was downloaded from the NOAA here). Plot the data 
and test whether it follows a random walk (with drift).

"""

# Import the adfuller function from the statsmodels module
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import pandas as pd

temp_NY = pd.read_excel('temp_NY.xlsx')
temp_NY = temp_NY.set_index('DATE')

# Convert the index to a datetime object
temp_NY.index = pd.to_datetime(temp_NY.index, format= '%Y')

# Plot average temperatures
temp_NY.plot()
plt.show()

# Compute and print ADF p-value
result = adfuller(temp_NY['TAVG'])
print("The p-value for the ADF test is ", result[1])

