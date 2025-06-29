import yfinance as yf
import pandas as pd
from datetime import datetime

def get_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    try:
        # Validate date formats and logic
        start_dt = datetime.strptime(start, "%Y-%m-%d")
        end_dt = datetime.strptime(end, "%Y-%m-%d")
        if start_dt > end_dt:
            print("Start date must be before end date.")
            return None
        if end_dt > datetime.today():
            print("End date cannot be in the future.")
            return None

        # Fetch stock data with raw Close prices
        data = yf.download(ticker, start=start, end=end, auto_adjust=False)

        if data.empty:
            print(f"No data found for ticker: {ticker} in the given date range.")
            return None

        # Flatten columns if multi-index (tuples)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        # Remove ticker suffix from column names like 'Close F' -> 'Close'
        data.columns = [
            col.replace(f" {ticker}", "") if isinstance(col, str) and col.endswith(f" {ticker}") else col
            for col in data.columns
        ]

        return data

    except ValueError as ve:
        print(f"Invalid date format. Use YYYY-MM-DD. Details: {ve}")
        return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    df = get_stock_data("F", "2024-01-01", "2024-01-15")
    if df is not None:
        print(df.head())
    else:
        print("Failed to fetch data.")
