import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm
import matplotlib.pyplot as plt

ticker = 'PETR4.SA'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2010-1-1')['Adj Close']

returns = np.log(1+data.pct_change())

rf = 0.0925
std = returns.std()*250**0.5
std = std.values
t = 1
intervals = 250
dt = t/intervals
n = 10000
z = np.random.standard_normal((intervals+1, n))
s = np.zeros_like(z)
d0 = data.iloc[-1]
s[0] = d0

for i in range(1,intervals+1):
  s[i] = s[i-1] * np.exp((rf-0.5*std**2)*dt+std*dt**0.5*z[i])

# plt.figure(figsize=(10,6))
# plt.plot(s[:, :10])
# plt.show()

strike = 35
p = np.maximum(s[-1]-strike,0)

price = np.exp(-rf*t)*np.sum(p)/n
print(price)