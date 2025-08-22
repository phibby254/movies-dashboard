import sys
import os
import requests

# Add the parent folder (mytrip) to Python's path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from paris_business_deals import get_deals

print("Bitcoin price checker running...")

# Example: show the deals
deals = get_deals()
print("💼 Paris Business Deals:")
for d in deals:
    print("-", d)


def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # raise error for bad response
        data = response.json()
        price = data["bitcoin"]["usd"]
        print(f"💰 Current Bitcoin Price: ${price:,.2f} USD")
    except requests.exceptions.RequestException as e:
        print("Error fetching Bitcoin price:", e)

if __name__ == "__main__":
    get_bitcoin_price()
