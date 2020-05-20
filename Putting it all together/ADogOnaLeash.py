# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:42:26 2020

@author: User


A Dog on a Leash? (Part 1)

The Heating Oil and Natural Gas prices are pre-loaded in DataFrames HO and NG. 
First, plot both price series, which look like random walks. Then plot the 
difference between the two series, which should look more like a mean reverting 
series (to put the two series in the same units, we multiply the heating oil 
prices, in $/gallon, by 7.25, which converts it to $/millionBTU, which is the 
same units as Natural Gas).

The data for continuous futures (each contract has to be spliced together in a 
continuous series as contracts expire) was obtained from Quandl.

"""

import matplotlib.pyplot as plt
import pandas as pd

HO = pd.read_excel('HO.xlsx')
HO = HO.set_index('Date')

NG = pd.read_excel('NG.xlsx')
NG = NG.set_index('Date')


# Plot the prices separately
plt.subplot(2,1,1)
plt.plot(7.25*HO, label='Heating Oil')
plt.plot(NG, label='Natural Gas')
plt.legend(loc='best', fontsize='small')

# Plot the spread
plt.subplot(2,1,2)
plt.plot(7.25*HO-NG, label='Spread')
plt.legend(loc='best', fontsize='small')
plt.axhline(y=0, linestyle='--', color='k')
plt.show()

#%%
"""
A Dog on a Leash? (Part 2)

To verify that Heating Oil and Natural Gas prices are cointegrated, First apply 
the Dickey-Fuller test separately to show they are random walks. Then apply the 
test to the difference, which should strongly reject the random walk hypothesis. 
The Heating Oil and Natural Gas prices are pre-loaded in DataFrames HO and NG.

"""

# Import the adfuller module from statsmodels
from statsmodels.tsa.stattools import adfuller

# Compute the ADF for HO and NG
result_HO = adfuller(HO['Close'])
print("The p-value for the ADF test on HO is ", result_HO[1])
result_NG = adfuller(NG['Close'])
print("The p-value for the ADF test on NG is ", result_NG[1])

# Compute the ADF of the spread
result_spread = adfuller(7.25 * HO['Close'] - NG['Close'])
print("The p-value for the ADF test on the spread is ", result_spread[1])











