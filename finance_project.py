# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 08:22:30 2020

@author: Wiley
"""

# Step 1: Import Libaries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import pandas_datareader
import datetime
import pandas_datareader.data as web


# Getting Data

start = datetime.datetime(2012,1,1)
end = datetime.datetime(2017,1,1)

tesla = web.DataReader('TSLA', 'yahoo',start,end)
ford = web.DataReader('F', 'yahoo', start,end)
gm = web.DataReader('GM', 'yahoo', start, end)

# Visualizing Data

tesla['Open'].plot(label = 'Tesla', figsize=(16,8), title ='Open Price')
gm['Open'].plot(label='GM')
ford['Open'].plot(label='Ford')
plt.legend()

tesla['Volume'].plot(label = 'Tesla', figsize=(16,8), title ='Volume Traded')
gm['Volume'].plot(label='GM')
ford['Volume'].plot(label='Ford')
plt.legend()

# What was the date of the Mximum trading volume for Ford?
# What happened that day?

ford['Volume'].argmax()

# Create a new column for each dataframe called "Total Traded" which is the
# Open Price multiplied by the Volume Traded.

tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
ford['Total Traded'] = ford['Open'] * ford['Volume']
gm['Total Traded'] = gm['Open'] * gm['Volume']

tesla['Total Traded'].plot(label = 'Tesla', figsize=(16,8))
gm['Total Traded'].plot(label='GM')
ford['Total Traded'].plot(label ='Ford')
plt.legend()

tesla['Total Traded'].argmax()

# Plot out some MA (Moving Average).
# Plot out the MA50 and MA200 for GM

gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA200'] = gm['Open'].rolling(200).mean()
gm[['Open','MA50','MA200']].plot(figsize = (16,8))

# See relationship between these stocks

from pandas.plotting import scatter_matrix

car_comp = pd.concat([tesla['Open'],gm['Open'],ford['Open']],axis = 1)

car_comp.columns = ['Tesla Open', 'GM Open', 'Ford Open']

scatter_matrix(car_comp, figsize = (8,8), alpha = 0.2)
