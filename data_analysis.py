import numpy as np
import pandas as pd

def calculate_moving_average(df, window=30):
    """
    Calculate the moving average of the closing prices.
    """
    return df['Close'].rolling(window=window).mean()

def calculate_bollinger_bands(df, window=30, num_sd=2):
    """
    Calculate Bollinger Bands.
    """
    rolling_mean = df['Close'].rolling(window=window).mean()
    rolling_std = df['Close'].rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * num_sd)
    lower_band = rolling_mean - (rolling_std * num_sd)
    return rolling_mean, upper_band, lower_band

def calculate_rsi(df, period=14):
    """
    Calculate the Relative Strength Index (RSI).
    """
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi
