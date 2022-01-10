import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel('./Housing.xlsx')
#print(data)

data_filtered = data[['House Price', 'House Size (sq.ft.)']]
# print(data_filtered)

x = data_filtered['House Size (sq.ft.)']
y = data_filtered['House Price']
# print(x,y)

# Chart
plt.scatter(x,y)
plt.axis([0,2500,0,1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft.)')
# plt.show()

# Table with regression values
x1 = sm.add_constant(x)
reg = sm.OLS(y,x1).fit()
res = reg.summary()
# print(res)

# Alpha, beta and r²
stats = stats.linregress(x,y)
beta = stats.slope
alpha = stats.intercept
rsquare = stats.rvalue ** 2

print('Alpha= '+str(alpha) + ', beta=' + str(beta) + ' and r^2=' + str(rsquare))

