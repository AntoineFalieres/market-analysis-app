import requests
import pendulum
import pandas as pd
import time

# --- 1. Define Parameters ---
SYMBOL = 'ETHBTC'
INTERVAL = '1w'  
LIMIT = 1000     
FILE_NAME = f"{SYMBOL}_{INTERVAL}_2_years_data.csv" # The name for your CSV file

# --- 2. Calculate Start Time using Pendulum ---
# Define the start time: 2 years ago, in UTC
two_years_ago = pendulum.now('UTC').subtract(years=2) 
start_time_ms = two_years_ago.int_timestamp * 1000

# --- 3. Define Endpoint and Headers ---
BASE_URL = 'https://api.binance.com/api/v3/klines'
URL = f"{BASE_URL}?symbol={SYMBOL}&interval={INTERVAL}&startTime={start_time_ms}&limit={LIMIT}"

if __name__ == '__main__':

    print(f"Fetching DAILY data for {SYMBOL} starting from: {two_years_ago.to_date_string()} (UTC)")
    print("-" * 60)

    # --- 4. Request Data ---
    try:
        response = requests.get(URL)
        response.raise_for_status() 
        raw_data = response.json()

        if not raw_data:
            print("No data retrieved. Exiting.")
            exit()

        print(f"Successfully retrieved {len(raw_data)} daily candles.")

        # --- 5. Process and Save Data to CSV ---
        
        # 5a. Define column headers for the Binance K-line data
        cols = [
            'Open time', 
            'Open', 
            'High', 
            'Low', 
            'Close', 
            'Volume', 
            'Close time', 
            'Quote asset volume', 
            'Number of trades', 
            'Taker buy base asset volume', 
            'Taker buy quote asset volume', 
            'Ignore'
        ]
        
        # 5b. Create DataFrame
        df = pd.DataFrame(raw_data, columns=cols)

        # 5c. Convert timestamp columns to readable datetime objects (using Pandas methods)
        # The timestamps are in milliseconds (Binance standard)
        df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
        df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')

        # 5d. Convert numerical columns (which are strings from the API) to float/numeric
        numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote asset volume', 
                        'Taker buy base asset volume', 'Taker buy quote asset volume']
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)
        
        # Optional: Set the Open Time as the DataFrame index
        df = df.set_index('Open time')

        # 5e. Save the DataFrame to a CSV file
        df.to_csv(FILE_NAME)

        print("-" * 60)
        print(f"✅ Data successfully saved to {FILE_NAME}")
        print(f"First 5 rows of saved data:\n{df.head()}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
    except Exception as e:
        print(f"An error occurred during data processing: {e}")