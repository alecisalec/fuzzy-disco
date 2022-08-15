#Rolling Averages
#Alec Graham
#8.14.22
#Description: get a visual representation
#of rolling averages of stock
#part 1 of Quantatative investment Strategy
#part 2 combine with Robin hood API


import numpy as numpy
import pandas
import requests 
import math
import xlsxwriter
import yfinance as yf
import matplotlib.pyplot as plt
import sys

#curl -XGET 'https://tradestie.com/api/v1/apps/reddit'


#command line arguments
ticker = sys.argv[1]
#print(ticker)
dateRange = sys.argv[2]
dateRange = int(dateRange)
#print(dateRange)
rollingAveRange = sys.argv[3]
rollingAveRange = int(rollingAveRange)
#print(rollingAveRange)


# ##Creating Moving averages Data with coca-cola stocks
Stock = yf.download(ticker)
stock=Stock.Close.to_frame()
# print(stock)
stock = stock.tail(dateRange)

### calculate moving averages calulated in 10 day windows
stockRoll=stock.rolling(window=rollingAveRange)
stockRoll=stockRoll.mean()
## show only last 30 days not entire historical data
stockRoll = stockRoll.tail(dateRange)

## configure the map output
plt.figure(figsize=(10,5))
plt.plot(stock, 'k-', label="original closing prices")
plt.plot(stockRoll, 'r-', label="rolling average")
plt.ylabel('Price')
plt.xlabel('Date')
plt.grid(linestyle=':')
plt.legend(loc='upper left')
plt.title(f"{ticker} over {dateRange} days with a {rollingAveRange} day rolling average period")
plt.show()
