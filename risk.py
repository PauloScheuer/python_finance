import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

assets = ['BRSR6.SA','ITSA4.SA']

data = pd.DataFrame()

for asset in assets:
  data[asset] = wb.DataReader(asset,data_source='yahoo',start='2010-1-1')['Adj Close']

#print(data.tail())

returns = np.log(data/data.shift(1))

#print(returns)

# Standard deviations
print('Comparison between volatilities:')
for asset in assets:
  print(asset)
  print('Returns: '+str(round(returns[asset].mean()*100,2))+'%') 
  print('Annual returns: '+str(round(returns[asset].mean() * 250 * 100,2))+'%')
  print('Standard deviation: '+str(round(returns[asset].std(),5)))
  print('Annual standard deviation: '+str(round(returns[asset].std() * 250 ** 0.5, 5)))
  print('\n')


# Covariance and correlation
print('Comparison between variances:')
for asset in assets:
  print(asset)
  print('Variance: '+str(round(returns[asset].var(),5))) 
  print('Annual variance: '+str(round(returns[asset].var() * 250 ,2)))
  print('\n')

print('Covariances:')
covariation = returns.cov()
print(covariation)

print('Correlations:')
correlation = returns.corr()
print(correlation)


# Portfolio risk
weights = np.array([0.5,0.5])

portfolio_var = np.dot(weights.T, np.dot(returns.cov()*250, weights))
print('\nPortfolio variance is '+str(portfolio_var))

portfolio_vol = (np.dot(weights.T, np.dot(returns.cov()*250, weights)))**0.5
print('\nPortfolio volatility is '+str(round(portfolio_vol*100,2))+'%')


# Diversifiable and non-diversifiable risk

diversifiable = portfolio_var
count = 0
for asset in assets:
  diversifiable = diversifiable - (weights[count]**2 * (returns[asset].var() * 250))
  count = count+1

print('\nDiversifiable risk is: '+str(round(diversifiable*100,2))+'%')
print('Non-Diversifiable risk is: '+ str(round((portfolio_var-diversifiable)*100,2))+'%')