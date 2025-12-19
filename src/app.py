import json
import streamlit as st
from providers.binance import BinanceProvider
from providers.coingecko import CoinGeckoProvider

# 1. Load the mappings
with open('data/crypto_symbols.json', 'r') as f:
    mappings = json.load(f)

# 2. UI: Let user select by Ticker (e.g., BTC)
selected_ticker = st.sidebar.selectbox("Select Asset", list(mappings.keys()))
asset_info = mappings[selected_ticker]

# 3. Use the correct ID based on the selected Source
source_choice = st.sidebar.radio("Data Source", ["Binance", "CoinGecko"])

if source_choice == "Binance":
    provider = BinanceProvider()
    query_id = asset_info["binance"]
else:
    provider = GeckoProvider()
    query_id = asset_info["coingecko"]

# 4. Fetch data using the translated ID
df = provider.get_candlestick_data(query_id, timeframe)