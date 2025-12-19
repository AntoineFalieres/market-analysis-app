import pandas as pd
from typing import List

def add_vwma(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """Calculates Volume Weighted Moving Average.
       Expects a DataFrame with 'close' and 'volume' columns.

    Args:
        df (DataFrame): DataFrame
        window (int, optional): Size of the moving window. Defaults to 20.

    Returns:
        float: Volume Weighted Moving Average (VWMA)
    """    
    # The Close price is usually used for price (P_i)
    # We need to ensure Close and Volume columns are numeric
    pv = df['close'] * df['volume']
    df['vwma'] = pv.rolling(window=window).sum() / df['volume'].rolling(window=window).sum()
    return df

def add_rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """Calculates Relative Strenght Index

    Args:
        df (pd.DataFrame): DataFrame
        period (int, optional): size of the period. Defaults to 14.

    Returns:
        float: _description_
    """
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))
    return df

def add_macd(df: pd.DataFrame):
    pass

def add_volume(df: pd.DataFrame):
    pass

def add_ema(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """Exponential Moving Average
    
    Args:
        df (DataFrame): DataFrame
        window (int, optional): Size of the moving window. Defaults to 20.

    Returns:
        pd.Dataframe
    """
    df[f'ema_{window}'] = df['close'].ewm(span=window, adjust=False).mean()
    return df

def add_bollinger_bands(df: pd.DataFrame, window: int = 20, std_dev: int = 2) -> pd.DataFrame:
    """Bollinger Bands (Upper, Middle, Lower)

    Args:
        df (pd.DataFrame): Dataframe
        window (int, optional): Size of the moving window. Defaults to 20.
        std_dev (int, optional): standard deviation. Defaults to 2.

    Returns:
        pd.DataFrame
    """
    sma = df['close'].rolling(window=window).mean()
    rstd = df['close'].rolling(window=window).std()
    df['bb_middle'] = sma
    df['bb_upper'] = sma + (std_dev * rstd)
    df['bb_lower'] = sma - (std_dev * rstd)
    return df