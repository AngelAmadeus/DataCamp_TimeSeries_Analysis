# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:18:28 2020

@author: User

Taxing Exercise: Compute the ACF
In the last chapter, you computed autocorrelations with one lag. Often we are 
interested in seeing the autocorrelation over many lags. The quarterly earnings 
for H&R Block (ticker symbol HRB) is plotted on the right, and you can see the 
extreme cyclicality of its earnings. A vast majority of its earnings occurs in 
the quarter that taxes are due.

You will compute the array of autocorrelations for the H&R Block quarterly 
earnings that is pre-loaded in the DataFrame HRB. Then, plot the autocorrelation 
function using the plot_acf module. This plot shows what the autocorrelation 
function looks like for cyclical earnings data. The ACF at lag=0 is always one, 
of course. In the next exercise, you will learn about the confidence interval 
for the ACF, but for now, suppress the confidence interval by setting alpha=1.

"""

# Import the acf module and the plot_acf module from statsmodels
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

HRB = pd.read_excel('HRB.xlsx')
HRB = pd.DataFrame(HRB)

# Convert date to index
HRB = HRB.set_index('Quarter')

# Compute the acf array of HRB
acf_array = acf(HRB)
print(acf_array)

# Plot the acf function
plot_acf(HRB, alpha = 1)
plt.show()