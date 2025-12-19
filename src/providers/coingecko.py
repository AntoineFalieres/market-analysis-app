import requests
import pandas as pd
from .base import CryptoProvider

class CoinGeckoProvider(CryptoProvider):
    def __init__(self):
        self.base_url = ""

    def get_history(self, symbol: str, interval: str, limit: int = 100) -> pd.DataFrame:
        params = {
            "symbol": symbol.upper(),
            "interval": interval,
            "limit": limit
        }
        
        response = requests.get(self.base_url, params=params)
        response.raise_for_status() # Raises error for bad status codes
        
        data = response.json()
        
        # Raw Binance data to DataFrame
        df = pd.DataFrame(data, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'
        ])

        # Clean up data
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        numeric_cols = ['open', 'high', 'low', 'close', 'volume']
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)

        # Keep only the standard columns defined in our "contract"
        df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
        
        return df