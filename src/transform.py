import pandas as pd


def transform_crypto_data(df):
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df = df.sort_values("date")
    df["return"] = df["price"].pct_change()

    return df
