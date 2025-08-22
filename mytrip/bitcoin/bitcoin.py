import requests

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
