# stock_market_analyzer/analysis.py
import pandas as pd

def calculate_moving_average(data: pd.DataFrame, windows=[20, 50]) -> pd.DataFrame:
    for window in windows:
        data[f"MA{window}"] = data['Close'].rolling(window=window).mean()
    return data

def calculate_rsi(data: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

def calculate_macd(data: pd.DataFrame) -> pd.DataFrame:
    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = exp1 - exp2
    data['Signal Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    return data

if __name__ == "__main__":
    # Simple test
    df = pd.DataFrame({
        'Close': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
    })
    print("Moving Averages:\n", calculate_moving_average(df))
    print("\nRSI:\n", calculate_rsi(df))
    print("\nMACD:\n", calculate_macd(df))
# stock_market_analyzer/analysis.py