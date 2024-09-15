# INF601 - Advanced Programming in Python
# Marcos German
# Mini Project 1

import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import os

stock_tickers = ['NFLX', 'MSFT', 'APPL', 'GOOGL', 'DIS']
data = {}

for stock_ticker in stock_tickers:
    stock = yf.Ticker(stock_ticker)
    history = stock.history(period='10d')
    data[stock_ticker] = history['Close'].tolist()

stock_arrays = {stock_ticker: np.array(prices) for stock_ticker, prices in data.items()}