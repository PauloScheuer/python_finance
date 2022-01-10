import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

# Predicting the future stock price of a company

ticker='B3SA3.SA'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2010-1-1')['Adj Close']

returns = np.log(1+data.pct_change())

# data.plot(figsize=(10,6))
# returns.plot(figsize=(10,6))
# plt.show()

avg = returns.mean()
var = returns.var()
std = returns.std()

drift = avg - (0.5*var)

intervals = 250
n = 5

# Daily returns:
d_returns = np.exp(drift.values + std.values * norm.ppf(np.random.rand(intervals,n)))
# print(d_returns)

day0 = data.iloc[-1]

prices = np.zeros_like(d_returns)
prices[0] = day0

for i in range(1,intervals):
  prices[i] = prices[i-1]*d_returns[i]

plt.figure(figsize=(10,6))
plt.plot(prices)
plt.show()


