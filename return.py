import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

ITSA = wb.DataReader('ITSA4.SA', data_source='yahoo', start='2010-1-1')
print('ITSA4: \n')
##############################################

# Rate of return (simple): (p1/p0) -1

ITSA['simple_return'] = (ITSA['Adj Close'] / ITSA['Adj Close'].shift(1)) - 1
#print(ITSA['simple_return'])

#ITSA['simple_return'].plot(figsize=(8,5))
#plt.show()

# Multiplying by 250 annualizes the value
avg_returns = ITSA['simple_return'].mean() * 250
print('The simple return is: ' + str(round(avg_returns*100,2))+'%')

##############################################

# Rate of return (logarithimic): log(p1/p0)

ITSA['log_return'] = np.log(ITSA['Adj Close'] / ITSA['Adj Close'].shift(1))
#print(ITSA['log_return'])

#ITSA['log_return'].plot(figsize=(8,5))
#plt.show()

# Multiplying by 250 annualizes the value
log_returns = ITSA['log_return'].mean() * 250
print('The logarithimic return is: ' + str(round(log_returns*100,2))+'%')

##############################################

# Portfoio return: use of weights for each asset

portfolio = ['ITSA4.SA', 'ABEV3.SA', 'VALE3.SA']
data = pd.DataFrame()
for item in portfolio:
  data[item] = wb.DataReader(item, data_source='yahoo', start='2010-1-1')['Adj Close']

# Dividing each value by the first one and then multiplying by 100 normalizes the values

data = (data / data.iloc[0] * 100)

returns = (data / data.shift(1)) -1
annual_returns = returns.mean()*250
weights = np.array([1/3,1/3,1/3])

print('\n\nThe simple return for the portfolio containing:')
for item in portfolio:
  print(item+';')
print('with equal weights is '+str(round(np.dot(annual_returns, weights)*100,2))+'%')