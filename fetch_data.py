# importing the necessary Python libraries to fetch and handle data
import requests  # make HTTP requests to external APIs
import json  # work with the data format (JSON) we get from the API

#  API endpoint
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    # request to fetch the data from the API
    response = requests.get(url)
    # Checking the Response
    if response.status_code == 200:
        # convert the response into JSON format 
        data = response.json()

        # To takes the data and saves it into a JSON file 
        with open('bitcoin_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully in bitcoin_data.json.")
    else:
        # If there's an issue, print the error code
        print(f"Failed to fetch data. Error Code: {response.status_code}")

except Exception as e:
    # Catching any potential errors and printing them
    print(f"An error occurred: {e}")
