
import requests
from datetime import datetime

# Function to fetch exchange rate for a given date
def get_exchange_rate(api_key, base_currency, target_currency, date=None):
    if date is None:  # If no date is specified, get current rate
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    else:  # If a date is specified, fetch historical rate
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/history/{base_currency}/{date}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if date is None:
            rate = data['conversion_rates'][target_currency]
            print(f"Current {base_currency} to {target_currency} rate: {rate}")
        else:
            rate = data['rates'][target_currency]
            print(f"Exchange rate on {date} for {base_currency} to {target_currency}: {rate}")
        return rate
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None

# Function to compare rates between two dates
def compare_rates(api_key, base_currency, target_currency, past_date):
    print("Fetching current exchange rate...")
    current_rate = get_exchange_rate(api_key, base_currency, target_currency)
    
    print(f"\nFetching exchange rate on {past_date}...")
    past_rate = get_exchange_rate(api_key, base_currency, target_currency, past_date)
    
    if current_rate and past_rate:
        difference = current_rate - past_rate
        print(f"\nDifference between current and {past_date} rates: {difference}")

if __name__ == "__main__":
    # Set your API key here
    API_KEY = 'your_api_key_here'  # Replace with your actual API key from exchangerate-api.com
    BASE_CURRENCY = 'USD'
    TARGET_CURRENCY = 'EUR'
    
    # Input the date you want to compare the exchange rate with (YYYY-MM-DD format)
    past_date = input("Enter a date to compare exchange rate (YYYY-MM-DD): ")

    # Ensure the date is valid
    try:
        datetime.strptime(past_date, '%Y-%m-%d')
        compare_rates(API_KEY, BASE_CURRENCY, TARGET_CURRENCY, past_date)
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
