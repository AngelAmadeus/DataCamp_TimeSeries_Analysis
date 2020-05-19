# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:14:25 2020

@author: User

Are We Confident This Stock is Mean Reverting?
In the last chapter, you saw that the autocorrelation of MSFT's weekly stock 
returns was -0.16. That autocorrelation seems large, but is it statistically 
significant? In other words, can you say that there is less than a 5% chance 
that we would observe such a large negative autocorrelation if the true 
autocorrelation were really zero? And are there any autocorrelations at other 
lags that are significantly different from zero?

Even if the true autocorrelations were zero at all lags, in a finite sample of 
returns you won't see the estimate of the autocorrelations exactly zero. In 
fact, the standard deviation of the sample autocorrelation is 1/N−−√ where N 
is the number of observations, so if N=100, for example, the standard deviation 
of the ACF is 0.1, and since 95% of a normal curve is between +1.96 and -1.96 
standard deviations from the mean, the 95% confidence interval is ±1.96/N−−√. 
This approximation only holds when the true autocorrelations are all

"""

# Import the plot_acf module from statsmodels and sqrt from math
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from math import sqrt

returns = pd.read_excel('returns.xlsx')
returns = pd.DataFrame(returns)

# Convert date to index
returns = returns.set_index('Date')

# Compute and print the autocorrelation of MSFT weekly returns
autocorrelation = returns['Adj Close'].autocorr()
print("The autocorrelation of weekly MSFT returns is %4.2f" %(autocorrelation))

# Find the number of observations by taking the length of the returns DataFrame
nobs = len(returns)

# Compute the approximate confidence interval
conf = 1.96/sqrt(nobs)
print("The approximate confidence interval is +/- %4.2f" %(conf))

# Plot the autocorrelation function with 95% confidence intervals and 20 lags using plot_acf
plot_acf(returns, alpha=0.05, lags = 20)
plt.show()

