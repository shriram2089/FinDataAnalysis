import requests
import pandas as pd

def fetch_stock_data(api_key, symbol, start_date, end_date):
    """
    Fetch historical stock data from Alpha Vantage API.
    """
    url = f"https://www.alphavantage.co/query"
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': 'full'
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'Time Series (Daily)' not in data:
        raise Exception(f"Error fetching data for symbol {symbol}: {data.get('Error Message', 'Unknown error')}")
    
    df = pd.DataFrame(data['Time Series (Daily)']).T
    df = df[['1. open', '2. high', '3. low', '4. close', '5. volume']]
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    
    df = df[(df.index >= start_date) & (df.index <= end_date)]
    df = df.astype(float)
    
    return df
