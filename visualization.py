import plotly.graph_objs as go
import plotly.express as px

def plot_stock_data(df, moving_average, upper_band, lower_band, rsi):
    """
    Plot stock data with moving average, Bollinger Bands, and RSI.
    """
    fig = go.Figure()

    # Price and Moving Average
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
    fig.add_trace(go.Scatter(x=df.index, y=moving_average, mode='lines', name='Moving Average'))

    # Bollinger Bands
    fig.add_trace(go.Scatter(x=df.index, y=upper_band, mode='lines', name='Upper Bollinger Band', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=df.index, y=lower_band, mode='lines', name='Lower Bollinger Band', line=dict(color='red')))

    # RSI
    fig.add_trace(go.Scatter(x=df.index, y=rsi, mode='lines', name='RSI', line=dict(color='purple'), yaxis='y2'))

    fig.update_layout(
        title='Stock Price Analysis',
        xaxis_title='Date',
        yaxis_title='Price',
        yaxis2=dict(title='RSI', overlaying='y', side='right'),
        template='plotly_dark'
    )

    fig.show()
