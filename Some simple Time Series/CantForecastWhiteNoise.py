# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:24:19 2020

@author: User

Can't Forecast White Noise
A white noise time series is simply a sequence of uncorrelated random variables 
that are identically distributed. Stock returns are often modeled as white noise. 
Unfortunately, for white noise, we cannot forecast future observations based on 
the past - autocorrelations at all lags are zero.

You will generate a white noise series and plot the autocorrelation function to 
show that it is zero for all lags. You can use np.random.normal() to generate 
random returns. For a Gaussian white noise process, the mean and standard deviation 
describe the entire process.

Plot this white noise series to see what it looks like, and then plot the 
autocorrelation function.
"""

# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf
import numpy as np
import matplotlib.pyplot as plt

# Simulate white noise returns
# loc = mean
# scale = desvest
returns = np.random.normal(loc=0.02, scale=0.05, size=1000)

# Print out the mean and standard deviation of returns
mean = np.mean(returns)
std = np.std(returns)
print("The mean is %5.3f and the standard deviation is %5.3f" %(mean,std))

# Plot returns series
plt.plot(returns)
plt.show()

# Plot autocorrelation function of white noise returns
plot_acf(returns, lags= 20)
plt.show()
