import requests

# Function to get exchange rates
def get_exchange_rates(base_currency='USD'):
    url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        return data['rates']
    else:
        print("Error fetching data")
        return None

# Function to convert currency
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == 'USD':
        converted_amount = amount * rates[to_currency]
    else:
        # Convert from another currency to USD first
        amount_in_usd = amount / rates[from_currency]
        converted_amount = amount_in_usd * rates[to_currency]
    
    return converted_amount

# Main function to run the converter
def currency_converter():
    # Get the exchange rates
    rates = get_exchange_rates()
    
    if rates is None:
        return
    
    # Currency options
    currencies = {
        'USD': 'United States Dollar',
        'EUR': 'Euro',
        'JPY': 'Japanese Yen',
        'GBP': 'British Pound Sterling',
        'AUD': 'Australian Dollar',
        'CAD': 'Canadian Dollar',
        'CHF': 'Swiss Franc',
        'CNY': 'Chinese Yuan Renminbi',
        'SEK': 'Swedish Krona',
        'NZD': 'New Zealand Dollar',
        'SGD': 'Singapore Dollar',
        'HKD': 'Hong Kong Dollar',
        'NOK': 'Norwegian Krone',
        'KRW': 'South Korean Won',
        'INR': 'Indian Rupee',
        'BRL': 'Brazilian Real',
        'MXN': 'Mexican Peso',
        'ZAR': 'South African Rand',
        'TRY': 'Turkish Lira',
        'RUB': 'Russian Ruble',
        'PLN': 'Polish Zloty',
        'DKK': 'Danish Krone',
        'THB': 'Thai Baht',
        'IDR': 'Indonesian Rupiah',
        'PHP': 'Philippine Peso',
        'MYR': 'Malaysian Ringgit',
        'HUF': 'Hungarian Forint',
        'CZK': 'Czech Koruna',
        'CLP': 'Chilean Peso',
        'PKR': 'Pakistani Rupee',
        'BDT': 'Bangladeshi Taka'
    }

    print("Available currencies:")
    for code, name in currencies.items():
        print(f"{code} - {name}")

    from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))

    if from_currency in rates and to_currency in rates:
        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency code entered.")

# Run the currency converter
currency_converter()
