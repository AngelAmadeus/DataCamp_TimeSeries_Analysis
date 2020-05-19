# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:33:09 2020

@author: User

Generate a Random Walk
Whereas stock returns are often modeled as white noise, stock prices closely f
ollow a random walk. In other words, today's price is yesterday's price plus 
some random noise.

You will simulate the price of a stock over time that has a starting price of 
100 and every day goes up or down by a random amount. Then, plot the simulated 
stock price. If you hit the "Run Code" code button multiple times, you'll see 
several realizations.

"""
import numpy as np
import matplotlib.pyplot as plt

# Generate 500 random steps with mean=0 and standard deviation=1
steps = np.random.normal(loc=0, scale=1, size=500)

# Set first element to 0 so that the first price will be the starting stock price
steps[0]=0

# Simulate stock prices, P with a starting price of 100
P = 100 + np.cumsum(steps)

# Plot the simulated stock prices
plt.plot(P)
plt.title("Simulated Random Walk")
plt.show()
