# python_finance
Collection of python scripts for stock analysis

#############

 - Each file works isolated;
 - They all (excluding regression.py, which uses a .xlsx as database) have at the beginning an array with the tickers to analyse;

# return.py
  Firstly, show the simple and the logarithmic return of a single stock. Then, shows the return of a portfolio.
  
# risk.py
  Compares volatilities of two stocks and shows the risk of a portfolio with them.
  
# regression.py
  The only one not related with the stock market. It uses a .xlsx with data about house prices to exemplify simple regressions.
  
# markowitz.py
  Simulates 1000 of combinations to plot in a chart the Markowitz Efficient Frontier.
  
# capm.py
  Uses the CAPM model to get the expected return of an asset. Also shows its sharpe ratio.
  
# grossprofit.py
  Using Monte Carlo simulations, it predicts the gross profit of a fictional company.
  
# stockprice.py
  Using Monte Carlo simulations, it predicts the stock price of a company defined in the variable 'ticker'.

# blackscholes.py and euler_discretization.py
  With different methods, both files price stock options.
