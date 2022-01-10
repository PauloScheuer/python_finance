import numpy as np
import matplotlib.pyplot as plt

# Predicting gross profit of an enterprise
revenue_avg = 100
revenue_std = 5
n = 1000

revenue = np.random.normal(revenue_avg,revenue_std,n)
# print(revenue)

# plt.figure(figsize=(10,6))
# plt.plot(revenue)
# plt.show()

COGS = -(revenue*np.random.normal(0.6,0.1))

# plt.figure(figsize=(10,6))
# plt.plot(COGS)
# plt.show()

# print(COGS.mean())
# print(COGS.std())

g_profit = revenue + COGS
# print(g_profit)
print('Max gross profit: '+ str(max(g_profit)))
print('Min gross profit: '+ str(min(g_profit)))
print('Avg gross profit: '+ str(g_profit.mean()))
print('Std gross profit: '+ str(g_profit.std()))

#Shows histogram with values
plt.figure(figsize=(10,6))
plt.hist(g_profit, bins=20)
plt.show()
