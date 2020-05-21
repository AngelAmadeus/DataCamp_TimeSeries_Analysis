# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:58:53 2020

@author: User



Getting "Warmed" Up: Look at Autocorrelations

Since the temperature series, temp_NY, is a random walk with drift, take first 
differences to make it stationary. Then compute the sample ACF and PACF. This 
will provide some guidance on the order of the model.

"""

# Import the modules for plotting the sample ACF and PACF
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

import matplotlib.pyplot as plt
import pandas as pd

temp_NY = pd.read_excel('temp_NY.xlsx')
temp_NY = temp_NY.set_index('DATE')

# Take first difference of the temperature Series
chg_temp = temp_NY.diff()
chg_temp = chg_temp.dropna()

# Plot the ACF and PACF on the same page
fig, axes = plt.subplots(2,1)

# Plot the ACF
plot_acf(chg_temp, lags=20, ax=axes[0])

# Plot the PACF
plot_pacf(chg_temp, lags=20, ax=axes[1])
plt.show()