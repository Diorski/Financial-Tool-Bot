import requests

# API Key (Replace 'YOUR_API_KEY' with your actual API key)
api_key = ""

#preparing the API request, defining the base URL for the Alpha vantage API


#Parameters for the Base URL
#//

def fetch_stock_data(symbol="AAPL"):
    # Set up the parameters for the API request
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "60min",
        "outputsize": "compact",
        "datatype": "json",
        "apikey": api_key,
    }
    # Make the GET request inside the function
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON format
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# This conditional ensures that the following code will run only if the script is executed directly,
# not when it's imported as a module in another script.
if __name__ == "__main__":
    try:
        # Call the function and print the data
        data = fetch_stock_data("AAPL")
        print(data)
    except Exception as e:
        print(e)
#//
#params = { -- this used to be my original function but now im making a definition for the funciton to make it more Modularity, Maintainability, seperation of concerns, flexibility)
   # "function": "TIME_SERIES_INTRADAY",
   # "symbol": "TD",  # stock symbol
   # "apikey": api_key,
   # "interval" : "5min", #interval time
   # "outputsize" : "compact", # Use "full" for more data  # compact which retuns on the latest 100 data points  
   # "datatype": "json"
#}
# using GET function to he Aplha Vatange API with the specified URL to grab the information 

#response = requests.get(base_url, params=params)

#Checking if the request was successful by checking the response's status code. Code 200 indiactes success

#if response.status_code == 200:
    #Convert the reponse to Json format 
 #   data = response.json()

    #print(data)
#else:
 #   print(f"Failed to fetch data: {response.status_code}")
