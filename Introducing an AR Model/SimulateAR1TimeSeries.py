# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:40:30 2020

@author: User

Simulate AR(1) Time Series
You will simulate and plot a few AR(1) time series, each with a different 
parameter, ϕ, using the arima_process module in statsmodels. In this exercise, 
you will look at an AR(1) model with a large positive ϕ and a large negative ϕ, 
but feel free to play around with your own parameters.

There are a few conventions when using the arima_process module that require 
some explanation. First, these routines were made very generally to handle both 
AR and MA models. We will cover MA models next, so for now, just ignore the MA 
part. Second, when inputting the coefficients, you must include the zero-lag 
coefficient of 1, and the sign of the other coefficients is opposite what we 
have been using (to be consistent with the time series literature in signal 
processing). For example, for an AR(1) process with ϕ=0.9, the array representing 
the AR parameters would be

"""

# import the module for simulating data
from statsmodels.tsa.arima_process import ArmaProcess
import matplotlib.pyplot as plt
import numpy as np

# Plot 1: AR parameter = +0.9
plt.subplot(2,1,1)
ar1 = np.array([1, -0.9])
ma1 = np.array([1])
AR_object1 = ArmaProcess(ar1, ma1)
simulated_data_1 = AR_object1.generate_sample(nsample=1000)
plt.plot(simulated_data_1)

# Plot 2: AR parameter = -0.9
plt.subplot(2,1,2)
ar2 = np.array([1, 0.9])
ma2 = np.array([1])
AR_object2 = ArmaProcess(ar2, ma2)
simulated_data_2 = AR_object2.generate_sample(nsample=1000)
plt.plot(simulated_data_2)
plt.show()
