# stock_market_analyzer/report_generator.py
import pandas as pd

def save_to_csv(data: pd.DataFrame, ticker: str):
    filename = f"{ticker}_report.csv"
    data.to_csv(filename)
    print(f"Report saved as {filename}")

def save_to_txt_report(data: pd.DataFrame, ticker: str):
    filename = f"{ticker}_report.txt"
    with open(filename, "w") as file:
        file.write(f"Stock Analysis Report for {ticker}\n\n")
        file.write("Summary (last 5 days):\n")
        file.write(str(data.tail()))
        file.write("\n\nInterpretation Tips:\n")

        # RSI interpretation
        if 'RSI' in data.columns:
            file.write("- RSI > 70 indicates the stock may be overbought (possible sell signal).\n")
            file.write("- RSI < 30 indicates the stock may be oversold (possible buy signal).\n")

        # MACD interpretation
        if 'MACD' in data.columns and 'Signal Line' in data.columns:
            file.write("- MACD crossing above Signal Line can indicate bullish momentum.\n")
            file.write("- MACD crossing below Signal Line can indicate bearish momentum.\n")

    print(f"Text report saved as {filename}")

if __name__ == "__main__":
    # Simple test
    import pandas as pd
    df = pd.DataFrame({
        'Close': [100, 101, 102, 103, 104],
        'RSI': [30, 40, 50, 60, 70],
        'MACD': [0.5, 0.4, 0.3, 0.2, 0.1],
        'Signal Line': [0.4, 0.3, 0.2, 0.1, 0.0],
        'MA20': [100, 101, 102, 103, 104],
        'MA50': [99, 100, 101, 102, 103]
    })
    save_to_csv(df, "TEST")
    save_to_txt_report(df, "TEST")
