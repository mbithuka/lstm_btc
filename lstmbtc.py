"""
grabs BTC-USD prices, and plots the closing price
"""
import math
import pandas_datareader as web
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
df = web.DataReader('BTC-USD', data_source = 'yahoo', start='2012-01-01', end = '2022-01-26')
plt.figure(figsize = (16,8))
plt.title('BTC Close Price History')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize = 18)
plt.ylabel('Close Price BTC', fontsize = 18)
plt.show()
