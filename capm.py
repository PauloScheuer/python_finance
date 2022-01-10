import numpy as np
import pandas as pd
from pandas_datareader import data as wb

assets = ['SAPR11.SA', '^BVSP']
data = pd.DataFrame()
for a in assets:
  data[a] = wb.DataReader(a, data_source='yahoo', start='2018-1-1', end='2021-12-31')['Adj Close']

returns = np.log(data/data.shift(1))
cov = returns.cov() * 250
# print(cov)

cov_with_market = cov.iloc[0,1]
# print(cov_market)

var_market = returns['^BVSP'].var()*250
# print(var_market)

# Beta calc
ASSET_beta = cov_with_market / var_market
#print('Beta: '+str(ASSET_beta))

# Brazilian risk free rate (SELIC): 9,25%
rf = 0.0925

prize = 0.05

# CAPM:
ASSET_return = rf + ASSET_beta * prize
print('The expected return for '+ assets[0] +' is: '+str(round(ASSET_return*100,2))+'% per year')

# Sharpe ratio
sharpe = (ASSET_return - rf) / (returns[assets[0]].std()*250 ** 0.5
print('The sharpe ratio for this asset is: '+str(sharpe))