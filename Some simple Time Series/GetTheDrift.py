# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:36:13 2020

@author: User

Get the Drift
In the last exercise, you simulated stock prices that follow a random walk. Y
ou will extend this in two ways in this exercise.

You will look at a random walk with a drift. Many time series, like stock prices, 
are random walks but tend to drift up over time.
In the last exercise, the noise in the random walk was additive: random, normal 
changes in price were added to the last price. However, when adding noise, you 
could theoretically get negative prices. Now you will make the noise 
multiplicative: you will add one to the random, normal changes to get a total 
return, and multiply that by the last price.

"""

import numpy as np
import matplotlib.pyplot as plt

# Generate 500 random steps
steps = np.random.normal(loc=0.001, scale=0.01, size=500) + 1

# Set first element to 1
steps[0]=1

# Simulate the stock price, P, by taking the cumulative product
P = 100 * np.cumprod(steps)

# Plot the simulated stock prices
plt.plot(P)
plt.title("Simulated Random Walk with Drift")
plt.show()