# market-analysis-app

Architecture 

```
crypto-analysis-tool/
├── .env                    # Secret API keys
├── .github/                # GitHub Actions for CI/CD
├── data/                   # Local cache or sample data (optional)
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py             # Entry point for local CLI or logic
│   ├── app.py              # Streamlit Entry point
│   │
│   ├── providers/          # API ADAPTERS (New)
│   │   ├── __init__.py
│   │   ├── base.py         # Abstract base class defining common methods
│   │   ├── binance.py      # Binance implementation
│   │   └── coingecko.py    # CoinGecko implementation
│   │
│   ├── logic/              # CORE LOGIC
│   │   ├── __init__.py
│   │   ├── indicators.py   # Math functions (VWMA, RSI, MACD, etc.)
│   │   └── processor.py    # Orchestrates fetching + adding indicators
│   │
│   └── ui/                 # UI COMPONENTS
│       ├── __init__.py
│       ├── charts.py       # Custom plotting logic (Plotly/Altair)
│       └── sidebar.py      # Input controls (API select, Indicators select)
└── tests/
│   ├── test_indicators.py
│   └── test_api.py
└── README.md               # Project documentation
```