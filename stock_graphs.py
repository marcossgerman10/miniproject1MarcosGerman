# INF601 - Advanced Programming in Python
# Marcos German
# Mini Project 1
from datetime import timedelta, datetime

import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import os

stock_tickers = ['NFLX', 'MSFT', 'AAPL', 'GOOGL', 'DIS']
data = {}

today = datetime.today()
ten_days_ago = today - timedelta(days=10)

for stock_ticker in stock_tickers:
    stock = yf.Ticker(stock_ticker)
    history = stock.history(start=ten_days_ago, end=today)
    data[stock_ticker] = history['Close'].tolist()

stock_arrays = {stock_ticker: np.array(prices) for stock_ticker, prices in data.items()}

if not os.path.exists('charts'):
    os.makedirs('charts')

for ticker, prices in stock_arrays.items():
    plt.plot(prices, marker='o')
    plt.title(f'{ticker} Closing Prices (Last 10 Days)')
    plt.xlabel('Days')
    plt.ylabel('Closing Price (USD)')
    plt.savefig(f'charts/{ticker}_closing_prices.png')
    plt.clf()
