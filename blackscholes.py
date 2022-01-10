import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm

def d1(S, K, r, std, T):
  return (np.log(S/K)+(r+std**2/2)*T) / (std*np.sqrt(T))

def d2(S, K, r, std, T):
  return (np.log(S/K)+(r-std**2/2)*T) / (std*np.sqrt(T))

def BS(S, K, r, std, T):
  return(S*norm.cdf(d1(S, K, r, std, T))) - (K*np.exp(-r*T) * norm.cdf(d2(S, K, r, std, T)))

ticker = 'PETR4.SA'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2010-1-1')['Adj Close']

s = data.iloc[-1]

returns = np.log(1+data.pct_change())
std = returns.std()*250**0.5

# Risk free rate
rf = 0.0925
# Strike
k = 35
# Time in years
t = 1

price = BS(s,k,rf,std,t)
print(price)