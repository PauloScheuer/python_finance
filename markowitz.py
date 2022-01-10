import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

assets = ['ABEV3.SA', '^BVSP']
data = pd.DataFrame()

for asset in assets:
  data[asset] = wb.DataReader(asset,data_source='yahoo',start='2010-1-1')['Adj Close']

# Show chart comparing both assets
# (data/data.iloc[0]*100).plot(figsize=(10,5))
#plt.show()

# Portfolio return, variance and volatility
returns = np.log(data/data.shift(1))
mean = returns.mean() * 250
cov = returns.cov()*250
corr = returns.corr()

n = len(assets)

p_returns = []
p_volatilities = []

for x in range(1000):
  weights = np.random.random(n)
  weights /= np.sum(weights)
  p_returns.append(np.sum(weights*mean))
  p_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(cov, weights))))

p_returns = np.array(p_returns)
p_volatilities = np.array(p_volatilities)

# print(p_returns, p_volatilities)

portfolios = pd.DataFrame({'Return':p_returns,'Volatility':p_volatilities})
portfolios.plot(x='Volatility',y='Return',kind='scatter',figsize=(10,6))
plt.xlabel('Expected volatility')
plt.ylabel('Expected return')
plt.show()