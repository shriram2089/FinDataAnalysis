import pandas as pd
from data_fetcher import fetch_stock_data
from data_analysis import calculate_moving_average, calculate_bollinger_bands, calculate_rsi
from visualization import plot_stock_data

def main():
    # Configuration
    API_KEY = 'YOUR_ALPHAVANTAGE_API_KEY'
    SYMBOL = 'AAPL'
    START_DATE = '2023-01-01'
    END_DATE = '2024-01-01'

    # Fetch data
    df = fetch_stock_data(API_KEY, SYMBOL, START_DATE, END_DATE)
    
    # Perform analysis
    moving_average = calculate_moving_average(df)
    rolling_mean, upper_band, lower_band = calculate_bollinger_bands(df)
    rsi = calculate_rsi(df)
    
    # Plot results
    plot_stock_data(df, moving_average, upper_band, lower_band, rsi)

if __name__ == "__main__":
    main()
