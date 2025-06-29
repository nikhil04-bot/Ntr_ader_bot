import yfinance as yf

def get_live_data():
    df = yf.download("^NSEBANK", interval="5m", period="1d")
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    return df
