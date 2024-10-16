# Currency-Converter
Steps to Run this code on GOOGLE COLAB 
Open Google Colab.
Create a new notebook.
# Install Required Libraries
You will need the requests library to fetch data from an API. You can install it using the following command:
!pip install requests
# Write the Code
# Overview
This code implements a simple currency converter that fetches the latest exchange rates from an API and allows users to convert an amount from one currency to another. It supports various currencies and displays available options to the user. The program is structured with functions to handle fetching exchange rates, converting currency amounts, and running the main converter logic.
# Explanation of the Code
# Importing Libraries: 
import requests
This line imports the requests library, which is used to make HTTP requests to retrieve data from the web.
# Function to Get Exchange Rates:
def get_exchange_rates(base_currency='USD'):
    ...
This function retrieves the current exchange rates for a specified base currency (default is USD).
It constructs a URL to access the exchange rate API and makes a GET request to fetch the data.
If the request is successful (status code 200), it returns the exchange rates; otherwise, it prints an error message.
# Function to Convert Currency:
def convert_currency(amount, from_currency, to_currency, rates):
    ...
This function takes an amount of money, the currency to convert from, the currency to convert to, and the exchange rates.
If the amount is in USD, it directly multiplies it by the exchange rate of the target currency.
If the amount is in another currency, it first converts it to USD and then to the target currency.
# Main Function to Run the Converter:
def currency_converter():
    ...
This is the main function that orchestrates the currency conversion process.
It calls get_exchange_rates to retrieve the latest rates.
It provides a list of available currencies and prompts the user for input on the currencies they wish to convert between and the amount.
It checks if the provided currency codes are valid and then calls convert_currency to perform the conversion. Finally, it prints the converted amount.
# Execution:
currency_converter()
This line executes the currency_converter function, starting the whole process.
# Summary
# In summary, the program allows users to convert currencies by fetching the latest exchange rates from an API, offering an interactive command-line interface to input desired currencies and amounts. It ensures that users have access to a variety of currency options while providing accurate conversion based on real-time data.






