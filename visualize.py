import matplotlib.pyplot as plt
import pandas as pd

def plot_stock_data(data: pd.DataFrame, ticker: str):
    # Flatten multi-index columns if present
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [' '.join(map(str, col)).strip() for col in data.columns.values]

    # Convert column names to strings just in case
    data.columns = [str(col) for col in data.columns]

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

    # Plot Close price and moving averages
    ax1.plot(data['Close'], label='Close Price', linewidth=2)  # <- FIXED HERE
    for col in data.columns:
        if isinstance(col, str) and col.startswith("MA"):
            ax1.plot(data[col], label=col, linestyle='--')
    ax1.set_title(f"Stock Price and Moving Averages for {ticker}")
    ax1.set_ylabel("Price (USD)")
    ax1.legend()
    ax1.grid(True)

    # Plot RSI
    if 'RSI' in data.columns:
        ax2.plot(data['RSI'], label='RSI', color='orange')
        ax2.axhline(70, color='red', linestyle='--')
        ax2.axhline(30, color='green', linestyle='--')
        ax2.set_ylabel("RSI")
        ax2.set_title("Relative Strength Index (RSI)")
        ax2.legend()
        ax2.grid(True)

    # Plot MACD and Signal Line
    if 'MACD' in data.columns and 'Signal Line' in data.columns:
        ax3.plot(data['MACD'], label='MACD', color='purple')
        ax3.plot(data['Signal Line'], label='Signal Line', color='blue')
        ax3.set_ylabel("MACD")
        ax3.set_title("MACD and Signal Line")
        ax3.legend()
        ax3.grid(True)

    plt.xlabel("Date")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    import numpy as np

    # Generate dummy test data
    dates = pd.date_range(start='2023-01-01', periods=50)
    data = pd.DataFrame({
        'Close': np.random.normal(100, 1, 50),
        'RSI': np.random.uniform(20, 80, 50),
        'MACD': np.random.normal(0, 1, 50), # Random MACD values
        'Signal Line': np.random.normal(0, 1, 50) # Random Signal Line values
    }, index=dates)     
    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()  
    plot_stock_data(data, "TEST")
# This code is for visualizing stock data, including close prices, moving averages, RSI, and MACD.
# It uses matplotlib to create a multi-panel plot.
# The main function generates dummy data for testing purposes.