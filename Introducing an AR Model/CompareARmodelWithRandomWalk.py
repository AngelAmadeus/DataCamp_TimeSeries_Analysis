# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:07:34 2020

@author: User


Compare AR Model with Random Walk

Sometimes it is difficult to distinguish between a time series that is slightly 
mean reverting and a time series that does not mean revert at all, like a random 
walk. You will compare the ACF for the slightly mean-reverting interest rate 
series of the last exercise with a simulated random walk with the same number 
of observations.

You should notice when plotting the autocorrelation of these two series 
side-by-side that they look very similar.

"""

# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
import pandas as pd


interest_rate_data = pd.read_excel('interest_rate_data.xlsx')
interest_rate_data = pd.DataFrame(interest_rate_data)

# Set date as index
interest_rate_data = interest_rate_data.set_index('DATE')


simulated_data = ([5.        , 4.77522278, 5.60354317, 5.96406402, 5.97965372,
       6.02771876, 5.5470751 , 5.19867084, 5.01867859, 5.50452928,
       5.89293842, 4.6220103 , 5.06137835, 5.33377592, 5.09333293,
       5.37389022, 4.9657092 , 5.57339283, 5.48431854, 4.68588587,
       5.25218625, 4.34800798, 4.34544412, 4.72362568, 4.12582912,
       3.54622069, 3.43999885, 3.77116252, 3.81727011, 4.35256176,
       4.13664247, 3.8745768 , 4.01630403, 3.71276593, 3.55672457,
       3.07062647, 3.45264414, 3.28123729, 3.39193866, 3.02947806,
       3.88707349, 4.28776889, 3.47360734, 3.33260631, 3.09729579,
       2.94652178, 3.50079273, 3.61020341, 4.23021143, 3.94289347,
       3.58422345, 3.18253962, 3.26132564, 3.19777388, 3.43527681,
       3.37204482])

# Plot the interest rate series and the simulated random walk series side-by-side
fig, axes = plt.subplots(2,1)

# Plot the autocorrelation of the interest rate series in the top plot
fig = plot_acf(interest_rate_data, alpha=1, lags=12, ax=axes[0])

# Plot the autocorrelation of the simulated random walk series in the bottom plot
fig = plot_acf(simulated_data, alpha=1, lags=12, ax=axes[1])

# Label axes
axes[0].set_title("Interest Rate Data")
axes[1].set_title("Simulated Random Walk Data")
plt.show()





