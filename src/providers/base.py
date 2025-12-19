from abc import ABC, abstractmethod
import pandas as pd

class CryptoProvider(ABC):
    """
    Abstract Base Class for all Crypto Data Providers.
    Any new API (Binance, Kraken, etc.) must implement these methods.
    """
    
    @abstractmethod
    def get_history(self, symbol: str, interval: str, limit: int) -> pd.DataFrame:
        """
        Fetches historical Klines/Candlestick data.
        Should return a DataFrame with: timestamp, open, high, low, close, volume.
        """
        pass

    def validate_data(self, df: pd.DataFrame):
        """Standard check to ensure the provider returns the correct columns."""
        required = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
        if not all(col in df.columns for col in required):
            raise ValueError(f"Provider returned incomplete data. Missing: {set(required) - set(df.columns)}")
        return True