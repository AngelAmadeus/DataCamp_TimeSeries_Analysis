# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:07:50 2020

@author: User


More Data Cleaning: Missing Data

When you print out the length of the DataFrame intraday, you will notice that 
a few rows are missing. There will be missing data if there are no trades in a 
particular one-minute interval. One way to see which rows are missing is to 
take the difference of two sets: the full set of every minute and the set of 
the DataFrame index which contains missing rows. After filling in the missing 
rows, you can convert the index to time of day and then plot the data.

Stocks trade at discrete one-cent increments (although a small percentage of 
trades occur in between the one-cent increments) rather than at continuous 
prices, and when you plot the data you should observe that there are long periods 
when the stock bounces back and forth over a one cent range. This is sometimes 
referred to as "bid/ask bounce".

"""

# Notice that some rows are missing
print("If there were no missing rows, there would be 391 rows of minute data")
print("The actual length of the DataFrame is:", len(intraday))

# Everything
set_everything = set(range(391))

# The intraday index as a set
set_intraday = set(intraday.index)

# Calculate the difference
set_missing = set_everything - set_intraday

# Print the difference
print("Missing rows: ", set_missing)

# Fill in the missing rows
intraday = intraday.reindex(range(391), method='ffill')

# Change the index to the intraday times
intraday.index = pd.date_range(start='2017-09-01 9:30', end='2017-09-01 16:00', freq='1min')

# Plot the intraday time series
intraday.plot(grid=True)
plt.show()

