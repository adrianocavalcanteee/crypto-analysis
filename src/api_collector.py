import requests
import pandas as pd


def get_crypto_data(crypto_id, days=365):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": days
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Erro na API: {response.status_code}")

    data = response.json()
    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "price"])

    return df
