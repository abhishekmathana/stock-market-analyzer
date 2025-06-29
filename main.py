from fetch_data import get_stock_data
from analysis import calculate_moving_average, calculate_rsi, calculate_macd
from visualize import plot_stock_data
from report_generator import save_to_csv, save_to_txt_report


def input_with_default(prompt, default):
    user_input = input(f"{prompt} (default: {default}): ")
    return user_input.strip() or default


def main():
    ticker = input_with_default("Enter stock ticker symbol (e.g., AAPL)", "F").upper()
    start_date = input_with_default("Enter start date (YYYY-MM-DD)", "2024-01-01")
    end_date = input_with_default("Enter end date (YYYY-MM-DD)", "2024-12-31")

    print(f"\nFetching data for {ticker} from {start_date} to {end_date}...")
    data = get_stock_data(ticker, start_date, end_date)

    if data is None or data.empty:
        print("Error fetching data or no data available.")
        return

    print("\nAvailable columns:", data.columns.tolist())
    if 'Close' not in data.columns:
        print("❌ ERROR: 'Close' column not found. Check if auto_adjust=False is set in fetch_data.py.")
        return

    print("\nCalculating indicators...")
    data = calculate_moving_average(data)
    data = calculate_rsi(data)
    data = calculate_macd(data)

    print("\nPlotting data...")
    plot_stock_data(data, ticker)

    print("\nSaving report...")
    save_to_csv(data, ticker)
    save_to_txt_report(data, ticker)

    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
