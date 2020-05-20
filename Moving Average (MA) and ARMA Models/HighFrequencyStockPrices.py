# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:23:22 2020

@author: User



High Frequency Stock Prices

Higher frequency stock data is well modeled by an MA(1) process, so it's a nice 
application of the models in this chapter.

The DataFrame intraday contains one day's prices (on September 1, 2017) for 
Sprint stock (ticker symbol "S") sampled at a frequency of one minute. The stock 
market is open for 6.5 hours (390 minutes), from 9:30am to 4:00pm.

Before you can analyze the time series data, you will have to clean it up a 
little, which you will do in this and the next two exercises. When you look at 
the first few rows (see the IPython Shell), you'll notice several things. First, 
there are no column headers.The data is not time stamped from 9:30 to 4:00, but 
rather goes from 0 to 390. And you will notice that the first date is the 
odd-looking "a1504272600". The number after the "a" is Unix time which is the 
number of seconds since January 1, 1970. This is how this dataset separates 
each day of intraday data.

If you look at the data types, you'll notice that the DATE column is an object, 
which here means a string. You will need to change that to numeric before you 
can clean up some missing data.

The source of the minute data is Google Finance (see here on how the data was 
downloaded).

The datetime module has already been imported for you.

"""

# import datetime module
import datetime
import pandas as pd


# Change the first date to zero
intraday.iloc[0,0] = 0

# Change the column headers to 'DATE' and 'CLOSE'
intraday.columns = ['DATE', 'CLOSE']

# Examine the data types for each column
print(intraday.dtypes)

# Convert DATE column to numeric
intraday['DATE'] = pd.to_numeric(intraday['DATE'])

# Make the `DATE` column the new index
intraday = intraday.set_index('DATE')



