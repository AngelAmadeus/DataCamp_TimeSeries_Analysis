# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:35:52 2020

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt


diet = pd.read_excel('diet.xlsx')
diet = pd.DataFrame(diet)

# Convert the date index to datetime
diet = diet.set_index('Date')
diet.index = pd.to_datetime(diet.index)

# Plot the entire time series diet and show gridlines
diet.plot(grid = True)
plt.show()

# From previous step
diet.index = pd.to_datetime(diet.index)

# Slice the dataset to keep only 2012
diet2012 = diet['2012']

# Plot 2012 data
diet2012.plot(grid = True)
plt.show()

