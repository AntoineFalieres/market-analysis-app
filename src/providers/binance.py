import requests
import pandas as pd
from .base import CryptoProvider

class BinanceProvider(CryptoProvider):
    def __init__(self):
        self.base_url = "https://api.binance.com/api/v3/klines"

    def get_candlestick_data(self, symbol: str, interval: str, limit: int = 100) -> pd.DataFrame:
        params = {
            "symbol": symbol.upper(),
            "interval": interval,
            "limit": limit
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            raw_data = response.json()
            
            # Binance returns a list of lists. We map it to columns.
            df = pd.DataFrame(raw_data, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'
            ])
            
            # Format types correctly
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            
            numeric_cols = ['open', 'high', 'low', 'close', 'volume']
            df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)
            
            # Return only the subset defined in the Base Class contract
            return df
            
        except Exception as e:
            print(f"Error fetching from Binance: {e}")
            return pd.DataFrame()