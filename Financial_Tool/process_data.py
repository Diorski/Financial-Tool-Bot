import pandas as pd
from fetch_stocks_data import fetch_stock_data
data = fetch_stock_data("AAPL")
print(list(data.keys()))

data = fetch_stock_data("AAPL")
# Try to create a DataFrame with the correct time series key
try:
    df = pd.DataFrame(data['Time Series (60min)']).T
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    df = df.apply(pd.to_numeric)
    
    # Normalize the 'Close' column
    df['Normalized Close'] = (df['Close'] - df['Close'].min()) / (df['Close'].max() - df['Close'].min())
    
    # Calculate intraday range and change percentage
    df['Intraday Range'] = df['High'] - df['Low']
    df['Change %'] = ((df['Close'] - df['Open']) / df['Open']) * 100
    

    # Print the first few rows of the DataFrame to observe the changes
    #print(df.head()) # or for just the first few rows
    pd.set_option('display.max_rows', None)
    
    #measures mean, mmedian, standard deviation
    print(df.describe())
    
    print(df) # Print the entire DataFrame or the first few rows to check the structure
    #print(data) # print the whole data set
except KeyError:
    print("Could not find the 'Time Series (5min)' key in the data. Check the JSON structure above.")
    exit()

    

    # Continue processing if the key is correct

df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True)
df = df.apply(pd.to_numeric)