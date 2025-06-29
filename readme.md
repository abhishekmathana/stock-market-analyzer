# Stock Market Analyzer

A Python application that fetches historical stock market data, calculates popular technical indicators (Simple Moving Average, Relative Strength Index, MACD), visualizes stock trends with plots, and generates CSV and text reports.

---

## Features

- Fetch historical stock data from Yahoo Finance using `yfinance`
- Calculate technical indicators:
  - Simple Moving Average (SMA)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
- Visualize stock price, moving averages, RSI, and MACD using matplotlib
- Generate CSV and TXT summary reports of analysis
- Command-line interface for easy use

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Required packages (install with pip):

```bash
pip install yfinance pandas matplotlib
git clone https://github.com/abhishekmathana/stock-market-analyzer.git
cd stock-market-analyzer
python main.py
